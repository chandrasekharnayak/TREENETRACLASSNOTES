from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from .forms import SignUpForm, LoginForm, PlanSelectionForm, PaymentForm
from .models import Order, Plan, Billing
import io
from reportlab.pdfgen import canvas


# User Sign Up
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:login')
    else:
        form = SignUpForm()
    return render(request, 'crm/signup.html', {'form': form})


# User Login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('crm:dashboard')
    else:
        form = LoginForm()
    return render(request, 'crm/login.html', {'form': form})


# User Dashboard: shows user name, active plan count, pending billing, and order history.
@login_required
def dashboard_view(request):
    user = request.user
    orders = Order.objects.filter(user=user)
    active_plans_count = orders.filter(order_status='activated').count()
    pending_billing = Billing.objects.filter(order__user=user, payment_status=False).count()
    context = {
        'user': user,
        'active_plans_count': active_plans_count,
        'pending_billing': pending_billing,
        'orders': orders,
    }
    return render(request, 'crm/dashboard.html', context)


# Plan Selection Page
@login_required
def select_plan_view(request):
    if request.method == 'POST':
        form = PlanSelectionForm(request.POST)
        if form.is_valid():
            plan_type = form.cleaned_data['plan_type']
            prepaid_plan = form.cleaned_data.get('prepaid_plan')
            billing_cycle = form.cleaned_data.get('billing_cycle')
            # For demo purposes, we set a fixed price
            price = 100.00
            plan = Plan.objects.create(
                plan_type=plan_type,
                prepaid_plan=prepaid_plan,
                billing_cycle=billing_cycle,
                price=price
            )
            # Create an order for the selected plan
            Order.objects.create(user=request.user, plan=plan)
            return redirect('crm:dashboard')
    else:
        form = PlanSelectionForm()
    return render(request, 'crm/select_plan.html', {'form': form})


# Order Management Page: display user orders and their statuses.
@login_required
def order_management_view(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'crm/order_management.html', {'orders': orders})


# Billing and Invoice Page: process payment and generate PDF invoice.
@login_required
def billing_invoice_view(request, order_id):
    try:
        order = Order.objects.get(id=order_id, user=request.user)
    except Order.DoesNotExist:
        return HttpResponse("Order not found", status=404)

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_type = form.cleaned_data['payment_type']
            # Simulate payment processing and mark billing as paid
            billing = Billing.objects.create(
                order=order,
                amount=order.plan.price,
                payment_type=payment_type,
                payment_status=True
            )
            # Generate PDF invoice using ReportLab
            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)
            p.drawString(100, 800, f"Invoice for Order #{order.id}")
            p.drawString(100, 780, f"User: {request.user.username}")
            p.drawString(100, 760, f"Plan: {order.plan}")
            p.drawString(100, 740, f"Amount: {billing.amount}")
            p.drawString(100, 720, f"Payment Type: {billing.payment_type}")
            p.showPage()
            p.save()
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename=f"invoice_order_{order.id}.pdf")
    else:
        form = PaymentForm(initial={'order_id': order.id})

    return render(request, 'crm/billing_invoice.html', {'form': form, 'order': order})
