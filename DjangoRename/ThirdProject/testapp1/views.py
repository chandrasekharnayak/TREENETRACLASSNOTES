from django.shortcuts import render
import datetime


# Create your views here.

def template_view(request):
    dt = datetime.datetime.now()
    name = 'Subhasish'
    age = 24
    salary = 89000

    my_dict = {'date':dt,'name':name,'age':age,'salary':salary}
    return render(request,'testapp1/resullt.html',context=my_dict)