from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

# Create your views here.
def request_views(request):
  # print(dir(request))
  # print(request.META)
  scheme = request.scheme
  body = request.body
  path = request.path
  host = request.get_host()
  method = request.method
  get = request.GET
  post = request.POST
  cookies = request.COOKIES
  return render(request,'01-request.html',locals())

def get_views(request):
  if 'name' in request.GET:
    print('name:'+request.GET['name'])
  if 'age' in request.GET:
    print('age:'+request.GET['age'])
  return HttpResponse('Get OK')

def post_views(request):
  # 判断请求方式，如果是get请求，则显示　03-post.html 模板
  if request.method == 'GET':
    return render(request,'03-post.html')
  # 如果是　post 请求，则获取请求提交的数据
  else:
    return HttpResponse('POST请求成功!')


def form_views(request):
  if request.method == 'GET':
    form = RemarkForm()
    return render(request,'04-form.html',locals())
  else:
    # subject = request.POST['subject']
    # email = request.POST['email']
    # message = request.POST['message']
    # topic = request.POST['topic']
    # isSaved = request.POST['isSaved']
    # print(subject,email,message,topic,isSaved)

    # 通过RemarkForm自动接收数据
    # 1.将request.POST数据传递给RemarkForm构造器
    form = RemarkForm(request.POST)
    # 2.验证form对象
    if form.is_valid():
      # 3.通过验证后获取具体的数据
      cd = form.cleaned_data
      subject = cd['subject']
      email = cd['email']
      isSaved = cd['isSaved']
      message = cd['message']
      topic = cd['topic']
      print(subject,email,isSaved,message,topic)
    return HttpResponse('Post OK')


def register_views(request):
  if request.method == 'GET':
    form = RegisterForm()
    return render(request,'05-register.html',locals())
  else:
    form = RegisterForm(request.POST)
    if form.is_valid():
      user = User(**form.cleaned_data)
      # 数据库配置成功并且实体类映射成表之后，该操作可以实现
      user.save()
    return HttpResponse('OK')

def login_views(request):
  if request.method == 'GET':
    form = LoginForm()
    #声明一个带有小部件的form - WidgetLoginForm
    # form = WidgetLoginForm()
    return render(request,'06-login.html',locals())

def setCookie_views(request):
  resp = HttpResponse('添加Cookie成功')
  resp.set_cookie('username','Wang Wc',60*60*24*7)
  return resp


def getCookie_views(request):
  # print(request.COOKIES)
  #　如果username在cookies中，则把username的值取出来，输出在终端上
  if 'username' in request.COOKIES:
    uname = request.COOKIES.get('username')
    print('用户名为:'+uname)
  return HttpResponse('Get Cookie OK')

def login09_views(request):
  if request.method == 'GET':
    #判断uname是否存在于cookies中，如果有的话，直接提示登录成功，否则，去往09-login模板
    if 'uname' in request.COOKIES:
      return HttpResponse('您已成功登录过')
    return render(request,'09-login.html')
  else:
    # 获取用户名称和密码
    uname=request.POST['uname']
    upwd = request.POST['upwd']
    # 判断用户名称和密码的
    if uname=='wangwc' and upwd=='123456':
      # 如果用户名和密码正确的话，判断有没有勾住记住密码
      resp = HttpResponse("登录成功")
      if 'isSaved' in request.POST:
        # 如果有勾住记住密码，则将用户名称保存进cookies
        resp.set_cookie('uname',uname,60*60*24*90)
      return resp
    else:
      return HttpResponse('登录失败')

def setSession_views(request):
  request.session['uname']='wangwc'
  return HttpResponse('Set Session Succefull')

def getSession_views(request):
  uname = request.session['uname']
  return HttpResponse('uname:'+uname)