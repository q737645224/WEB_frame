from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index01(request):
    return HttpResponse("index")