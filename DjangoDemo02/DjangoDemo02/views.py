from django.http import HttpResponse
from django.shortcuts import render

from django.template import loader

# def var_views(request):
#     t = loader.get_template('02-var.html')
#     dic = {
#         '姓名':"王",
#         '年龄':30,
#         '性别':"男",
#         "喜欢一句话":'天下'
#     }
#     html = t.render(dic)
#     return HttpResponse(html)

def var01_views(request):
    dic = {
        '变量名1': '值1',
        '变量名2': '值2',
    }
    return render(request, '02-var.html', dic)