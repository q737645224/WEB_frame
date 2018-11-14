from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_views(request):
  return HttpResponse("这是music应用中的index访问路径")

def test01_views(request):
  return HttpResponse('这是没有参数的test访问路径')

def test02_views(request,num):
  return HttpResponse('传递进来的参数为:'+num)