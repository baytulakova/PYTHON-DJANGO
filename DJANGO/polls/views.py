from django.http import HttpResponse
from django.shortcuts import render

# from .models import Category

def index(request):
    return render(request, 'polls/index.html', )

def category(request):
    return render(request, 'polls/site1.html', )

def phones(request):
    return render(request,'polls/site2.html',)

def proc(request):
    return render(request,'polls/site3.html',)

def op(request):
    return render(request,'polls/site4.html',)

def usb(request):
    return render(request,'polls/site5.html',)

def zakaz(request):
    return render(request,'polls/site6.html',)
