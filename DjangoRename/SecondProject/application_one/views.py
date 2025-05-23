from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def date_time_view(request):
    date = datetime.datetime.now()
    s = '<h1>The currenet Date and Time at server is :-'+str(date)+'</h1>'
    return HttpResponse(s)

def good_morning(request):
    return HttpResponse('<h1> Hello all Good Morning</h1>')

def good_afternoon(request):
    return HttpResponse('<h1> Hello all Good Afternoon</h1>')

def good_evening(request):
    return HttpResponse('<h1> Hello all Good evening</h1>')


# FBV
