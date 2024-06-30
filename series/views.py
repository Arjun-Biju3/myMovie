from django.shortcuts import render
from series.models import Series
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
    return render(request,'details2.html')