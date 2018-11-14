from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
def temp_views(request):
  #通过　loader 加载模板得到模板对象 t
  # t = loader.get_template('01-template.html')
  #通过　t 将模板渲染成字符串得到　html
  # html = t.render()
  #通过　HttpResponse() 将html构建成响应内容并返回
  # return HttpResponse(html)

  #通过 render() 完成模板的加载并响应
  return render(request,'01-template.html')


def var_views(request):
  name = '王老师'
  age = 30
  gender = '男'
  message = '天下没有吃不散的宴席'
  tup = ('王老师',"MrWang","Rap Wang")
  list = ['NARUTO','SASUKE','SAKURA']
  dic = {
    'BJ':'北京',
    'SY':'沈阳',
    'CC':'长春',
  }
  show = showMsg()
  dog = Dog()
  dog.name = '小强'
  return render(request,'02-var.html',locals())

def static_views(request):
  return render(request,'03-static.html')







def showMsg():
  return "This is a function"

class Dog(object):
  name = "旺财"
  age = 7

  def eat(self):
    return "吃狗粮"