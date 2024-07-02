from django.shortcuts import render,redirect
from Movies.models import Movies,Genere,MovieComments,MovieReview
from series.models import Series
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    home=Movies.objects.order_by('-id')[:4]
    expected=Series.objects.order_by('-id')[:6]
    new_m=Movies.objects.order_by('priority')[:3]
    new_s=Series.objects.order_by('priority')[:3]
    movie_new=Movies.objects.order_by('-id')[:12]
    series_new=Series.objects.order_by('-id')[:12]
    context={'home':home,'expected':expected,'new_m':new_m,'new_s':new_s,'movie_new':movie_new,'series_new':series_new}
    return render(request,'index.html',context)

@login_required(login_url='signup')
def movie_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    movies=Movies.objects.order_by('priority')
    movie_paginator=Paginator(movies,18)
    movie_lst=movie_paginator.get_page(page)
    context={'movies':movie_lst}
    return render(request,'movie_list.html',context)

@login_required(login_url='signup')
def details(request,pk):
    if request.POST and 'comment_m' in request.POST:
        try:
            comment=request.POST.get('comment')
            user=request.user
            usr=user.user_profile
            owner=Movies.objects.get(pk=pk)
            comment=MovieComments.objects.create(owner=owner,user=usr,comment=comment)
            success_message="comment added successfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="Fields should not be empty"
            messages.error(request,error_message)
    if request.POST and 'review_m' in request.POST:
        try:
            review=request.POST.get('review')
            print(review)
            title=request.POST.get('title')
            rating=request.POST.get('rating')
            usr=request.user
            user=usr.user_profile
            owner=Movies.objects.get(pk=pk)
            review=MovieReview.objects.create(owner=owner,user=user,review=review,title=title,rating=rating)
            success_message="review added successfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="Fields should not be empty"
            messages.error(request,error_message)
            
    obj=Movies.objects.get(pk=pk)
    movie=Movies.objects.get(pk=pk)
    rating=movie.rating
    related=Movies.objects.filter(rating=rating).exclude(pk=pk)[:6]
    comments=MovieComments.objects.filter(owner=movie)
    review=MovieReview.objects.filter(owner=movie)
    context={'movie':obj,'related':related,'comments':comments,'review':review}
    return render(request,'details1.html',context)

def search(request):
    if request.POST:
        search=request.POST.get('search')
        movie=Movies.objects.filter(name__contains=search)
        series=Series.objects.filter(name__contains=search)
        context={'movie':movie,'series':series}
    return render(request,'search.html',context)