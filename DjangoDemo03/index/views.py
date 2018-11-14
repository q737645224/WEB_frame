from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def parent_views(request):
    return render(request, '01-parent.html')

def child_views(request):
    return render(request, '02-child.html')


def index_views(request):
    return render(request,'index.html')

def login_views(request):
    return render(request,'login.html')

def register_views(request):
    return render(request,'register.html')

