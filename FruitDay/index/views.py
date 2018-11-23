import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

from index.forms import *
from index.models import *


def cart_views(request):
    return render(request,'Cart.html')
def index_views(request):
    return render(request,'index.html')
def login_views(request):
    if request.method =='GET':
        url = request.META.get('HTTP_REFERER','/')
        # print(url)
        if 'uphone' in request.session and 'uid' in request.session:
            return redirect(url)
        else:
            if 'uphone' in request.COOKIES and 'uid' in request.COOKIES:
                request.session['uid'] = request.COOKIES.get('uid')
                request.session['uphone'] = request.COOKIES.get('uphone')
                return redirect(url)
            else:
                form = UsersForm()
                url = url
                return render(request,'login.html',locals())
    else:
        url = request.POST.get('url')
        form = UsersForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            uphone = cd['uphone']
            upwd = cd['upwd']
            user = Users.objects.get(uphone=uphone)
            if user.upwd == upwd:
                request.session['uid'] = user.id
                request.session['uphone'] = uphone
                resp = redirect(url)
                if 'isSave' in request.POST:
                    resp.set_cookie('uid',user.id,expires=60*60*24*365)
                    resp.set_cookie('uphone',uphone,expires=60*60*24*365)
                return resp
            else:
                return redirect(url)
def register_views(request):
    return render(request,'register.html')

def logout_views(request):
    url = request.META.get('HTTP_REFERER', '/')
    resp = redirect(url)
    # 判断登录信息是否在session中
    if 'uid' in request.session and 'uphone' in request.session:
        del request.session['uid']
        del request.session['uphone']
    if 'uid' in request.COOKIES and 'uphone' in request.COOKIES:
        resp.delete_cookie('uid')
        resp.delete_cookie('uphone')
    return resp

def check_login(request):
    if 'uid' in request.session and 'uphone' in request.session:
        user = Users.objects.get(id=request.session.get('uid'))
        uname = user.uname
        dic = {
            'loginStatus': 1,
            "uname": uname,
        }
    else:
        if 'uid' in request.COOKIES and 'uphone' in request.COOKIES:
            request.session['uid'] = request.COOKIES.get('uid')
            request.session['upone'] = request.COOKIES.get('uphone')
            user = Users.objects.get(id=request.session.get('uid'))
            uname = user.uname
            dic = {
                'loginStatus': 1,
                "uname": uname,
            }
        else:
            dic = {
                'loginStatus': 0,
            }
    return HttpResponse(json.dumps(dic))

def check_repetion(request):
    uphone = request.GET.get('uphone')

    try:
        user = Users.objects.get(uphone=uphone)
        dic = {
            "registerStatus":1,
            'msg':'该手机号已存在'
        }
    except Exception as e:
        dic={
            "registerStatus":0,
            'msg':'该手机号可以注册',
        }
    return HttpResponse(json.dumps(dic))

def load_type_goods(request):
    all_list = []
    #读取goodsType下的所有的内容
    types = GoodsType.objects.all()
    for type in types:
        type_json = json.dumps(type.to_dict())
        goods = type.goods_set.all()[0:10]
        goods_json = serializers.serialize('json',goods)
        dic = {
            'type':type_json,
            'goods':goods_json,
        }
        all_list.append(dic)
    return HttpResponse(json.dumps(all_list))