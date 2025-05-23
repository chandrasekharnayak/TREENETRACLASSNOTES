from django.urls import path
from . import views

app_name = 'crm'
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('select_plan/', views.select_plan_view, name='select_plan'),
    path('order_management/', views.order_management_view, name='order_management'),
    path('billing_invoice/<int:order_id>/', views.billing_invoice_view, name='billing_invoice'),
]


# http://127.0.0.1:8000/signup/