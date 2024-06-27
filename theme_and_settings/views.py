from django.shortcuts import render

def about_us(request):
    return render(request,'about.html')

def help(request):
    return render(request,'faq.html')
    