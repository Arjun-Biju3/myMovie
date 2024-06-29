from django.shortcuts import render
from Movies.models import Movies,Genere
from series.models import Series

def home(request):
    home=Movies.objects.order_by('-id')[:4]
    expected=Series.objects.order_by('-id')[:6]
    new_m=Movies.objects.order_by('priority')[:3]
    new_s=Series.objects.order_by('priority')[:3]
    context={'home':home,'expected':expected,'new_m':new_m,'new_s':new_s}
    return render(request,'index.html',context)

def movie_list(request):
    return render(request,'movie_list.html')
