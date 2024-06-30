from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from customers.models import Customer
from django.contrib import messages

def sign_up(request):
    if request.POST:
        try:
            name=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            #register user
            user=User.objects.create_user(
                username=email,
                password=password,
                email=email
            )
            customer=Customer.objects.create(
                name=name,
                email=email,
                password=password,
                user=user
            )
            success_message="User registered succesfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="Duplicte username or invalid inputs"
            messages.error(request,error_message)
    return render(request,'signup.html')

def sign_in(request):
    if request.POST:
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(username=email,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid user credentials')
    return render(request,'signin.html')

def sign_out(request):
    logout(request)
    return redirect('home')