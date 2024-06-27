from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def movie_list(request):
    return render(request,'movie_list.html')
