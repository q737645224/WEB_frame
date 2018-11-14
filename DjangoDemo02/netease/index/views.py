from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_views(request):
  return HttpResponse("这是网站的首页")

def login_views(request):
  return HttpResponse("这是登录页面")

def register_views(request):
  return HttpResponse("这是注册页面")
