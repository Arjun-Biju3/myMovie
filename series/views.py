from django.shortcuts import render
from series.models import Series,Season,SeriesComments,SeriesReview
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='signup')
def series_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    series=Series.objects.order_by('priority')
    series_paginator=Paginator(series,18)
    series_lst=series_paginator.get_page(page)
    context={'series':series_lst}
    return render(request,'series_list.html',context)

@login_required(login_url='signup')
def view_deatils(request,pk):
    if request.POST and 'comment_s' in request.POST:
        try:
            comment=request.POST.get('comment')
            user=request.user
            usr=user.user_profile
            owner=Series.objects.get(pk=pk)
            comment=SeriesComments.objects.create(owner=owner,user=usr,comment=comment)
            success_message="comment added successfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="Fields should not be empty"
            messages.error(request,error_message)
            
    if request.POST and 'review_s' in request.POST:
        try:
            title=request.POST.get('title')
            review=request.POST.get('review')
            rating=request.POST.get('rating')
            user=request.user
            usr=user.user_profile
            owner=Series.objects.get(pk=pk)
            review=SeriesReview.objects.create(owner=owner,user=usr,rating=rating,review=review,title=title)
            success_message="review added successfully"
            messages.success(request,success_message)
        except Exception as e:
            error_message="Fields should not be empty"
            messages.error(request,error_message)
    obj=Series.objects.get(pk=pk)
    series=Series.objects.get(pk=pk)
    rating=series.rating
    related=Series.objects.filter(rating=rating).exclude(pk=pk)[:6]
    season=Season.objects.filter(owner=series)
    comments=SeriesComments.objects.filter(owner=series)
    review=SeriesReview.objects.filter(owner=series)
    context={'series':obj,'related':related,'season':season,'comments':comments,'review':review}
    return render(request,'details2.html',context)