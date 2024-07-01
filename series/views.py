from django.shortcuts import render
from series.models import Series,Season,SeriesComments,SeriesReview
from django.core.paginator import Paginator

def series_list(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    series=Series.objects.order_by('priority')
    series_paginator=Paginator(series,18)
    series_lst=series_paginator.get_page(page)
    context={'series':series_lst}
    return render(request,'series_list.html',context)


def view_deatils(request,pk):
    if request.POST:
        comment=request.POST.get('comment')
        user=request.user
        usr=user.user_profile
        owner=Series.objects.get(pk=pk)
        comment=SeriesComments.objects.create(owner=owner,user=usr,comment=comment)
    obj=Series.objects.get(pk=pk)
    series=Series.objects.get(pk=pk)
    rating=series.rating
    related=Series.objects.filter(rating=rating).exclude(pk=pk)[:6]
    season=Season.objects.filter(owner=series)
    comments=SeriesComments.objects.filter(owner=series)
    context={'series':obj,'related':related,'season':season,'comments':comments}
    return render(request,'details2.html',context)