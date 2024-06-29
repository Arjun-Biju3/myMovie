from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from customers.models import Customer
from django.contrib import messages

def sign_up(request):
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        #register user
        user=User.objects.create_user(
            username=email,
            password=password,
            email=email
        )
        customer=Customer.objects.craete(
            name=name,
            email=email,
            password=password,
            user=user
        )
    return render(request,'signup.html')

def sign_in(request):
    return render(request,'signin.html')
