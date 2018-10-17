from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#coding:utf-8
def index(request):
       #return HttpResponse(u"Hello World! 大家好！")
       # return HttpResponse(u“Hello World!大家好！”)
       return render(request,"index.html")
