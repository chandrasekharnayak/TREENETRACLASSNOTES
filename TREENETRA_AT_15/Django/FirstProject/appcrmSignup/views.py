from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def signup_view(request):
    '''This function focus on sign up page, whne a new user will some, hit this page an create a account'''
    if request.method =="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username already exits')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'Account created successfully')
                return 'login'
        else:
            messages.error(request,'Password do not match')
    return render(request,'signup.html')


#login view after sign up
def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid credentials')
    return render(request,'login.html')


#Dashboard

def dashboard_view(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('login')

#logout_view

def logout_view(request):
    logout(request)
    return redirect('login')




