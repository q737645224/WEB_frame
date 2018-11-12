from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def new01(request):
    return HttpResponse('news')
