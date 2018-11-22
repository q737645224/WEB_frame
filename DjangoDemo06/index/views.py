import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from index.forms import *
from index.models import Author


def request_views(request):
  scheme = request.scheme
  body = request.body
  path = request.path
  full_path = request.get_full_path()
  host = request.get_host()
  method = request.method
  post = request.POST
  get = request.GET
  cookies = request.COOKIES
  meta = request.META
  return render(request,'01-request.html',locals())

def request02_views(request):
  year = request.GET.get('year','1900')
  month = request.GET.get('month','01')
  day = request.GET.get('day','01')
  print("传递的数据:%s年%s月%s日" % (year,month,day))
  return HttpResponse('Get OK')

def post_views(request):
  if request.method == 'GET':
    return render(request,'03-post.html')
  else:
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    return HttpResponse("用户名:%s,用户密码:%s" % (uname,upwd))

def all_views(request):
  authors = Author.objects.all()
  for au in authors:
    print(au.id,au.name,au.age,au.email)
  return HttpResponse("Query OK")

def register_views(request):
  if request.method == 'GET':
    return render(request,'05-register.html')
  else:
    #接收前端传递过来的数据
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')
    #将数据封装成 author 的对象
    au = Author()
    au.name = name
    au.age = age
    au.email = email
    #调用author的save()将数据保存进数据库
    au.save()
    return HttpResponse("Register OK")

def form_views(request):
  if request.method == 'GET':
    #创建RemarkForm的对象,并发送到06-form.html中
    form = RemarkForm()
    return render(request,'06-form.html',locals())
  else:
    # subject = request.POST.get('subject')
    # email = request.POST.get('email')
    # message = request.POST.get('message')
    # topic = request.POST.get('topic')
    # isSaved = request.POST.get('isSaved','0')

    #使用forms的对象来接收提交的数据
    #1.将request.POST的数据提交给RemarkForm
    form = RemarkForm(request.POST)
    #2.让RemarkForm的对象通过验证
    if form.is_valid():
      #3.通过验证后再获取各个控件的值
      cd = form.cleaned_data
      print(cd['email'],cd['subject'])

      return HttpResponse("Post OK")
      # return HttpResponse("Subject:%s,Email:%s,Message:%s,Topic:%s,IsSaved:%s" % (subject,email,message,topic,isSaved))

def form_register(request):
  if request.method == 'GET':
    form = RegisterForm()
    return render(request,'07-form-register.html',locals())
  else:
    # 将request.POST中的数据提交给RegisterForm()
    form = RegisterForm(request.POST)
    # 将数据通过验证
    if form.is_valid():
      # 验证过后获取数据并保存进数据库
      au = Author(**form.cleaned_data)
      au.save()
      return HttpResponse("Register OK")

def widget1_views(request):
  if request.method == 'GET':
    form = WidgetForm1()
    return render(request,'08-widget1.html',locals())

def widget2_views(request):
  if request.method == 'GET':
    form = WidgetForm2()
    return render(request,'08-widget1.html',locals())

def setcookie_views(request):
  resp = HttpResponse('添加Cookie成功')
  #保存cookie的值到resp中
  resp.set_cookie('test_name','wangwc',60*60*24*365)
  return resp

def getcookie_views(request):
  if 'test_name' in request.COOKIES:
    value = request.COOKIES.get('test_name')
    return HttpResponse("test_name的值为:"+value)
  else:
    return HttpResponse('cookie中没有您要找的值')

def ajax_views(request):
  return render(request,'12-ajax.html')

def server12_views(request):
  # list = ["NARUTO","HINATA","SAKURA","SASUKE"]
  # jsonStr = json.dumps(list)

  #查询Author中所有的数据
  # authors=Author.objects.all()
  #将authors转换为json格式的字符串
  # jsonStr=serializers.serialize('json',authors)
  # print(jsonStr)

  #查询id为2的Author的数据
  # author=Author.objects.get(id=2)
  # 以下写法错误:serialize()只能将查询结果集转换成json,单个对象则不可以
  # jsonStr=serializers.serialize('json',author)

  # 以下方式写法正确
  # authors = Author.objects.filter(id=2)
  # jsonStr=serializers.serialize('json',authors)

  author=Author.objects.get(id=2)
  jsonStr=json.dumps(author.to_dict())
  return HttpResponse(jsonStr)

def ajax_post(request):
  return render(request,'13-post.html')

def server13_views(request):
  uname = request.POST['uname']
  uage = request.POST['uage']
  return HttpResponse("uname:%s,uage:%s" % (uname,uage))