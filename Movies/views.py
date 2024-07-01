from django.shortcuts import render
from Movies.models import Movies,Genere,MovieComments,MovieReview
from series.models import Series
from django.core.paginator import Paginator

def home(request):
    home=Movies.objects.order_by('-id')[:4]
    expected=Series.objects.order_by('-id')[:6]
    new_m=Movies.objects.order_by('priority')[:3]
    new_s=Series.objects.order_by('priority')[:3]
    movie_new=Movies.objects.order_by('-id')[:12]
    series_new=Series.objects.order_by('-id')[:12]
    context={'home':home,'expected':expected,'new_m':new_m,'new_s':new_s,'movie_new':movie_new,'series_new':series_new}
    return render(request,'index.html',context)

def movie_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    movies=Movies.objects.order_by('priority')
    movie_paginator=Paginator(movies,18)
    movie_lst=movie_paginator.get_page(page)
    context={'movies':movie_lst}
    return render(request,'movie_list.html',context)


def details(request,pk):
    if request.POST:
        comment=request.POST.get('comment')
        user=request.user
        usr=user.user_profile
        owner=Movies.objects.get(pk=pk)
        comment=MovieComments.objects.create(owner=owner,user=usr,comment=comment)
    obj=Movies.objects.get(pk=pk)
    movie=Movies.objects.get(pk=pk)
    rating=movie.rating
    related=Movies.objects.filter(rating=rating).exclude(pk=pk)[:6]
    comments=MovieComments.objects.filter(owner=movie)
    context={'movie':obj,'related':related,'comments':comments}
    return render(request,'details1.html',context)