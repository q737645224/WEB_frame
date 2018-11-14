from django.conf.urls import url
from .views import *
# 匹配　http://localhost:8000/music/ 后的具体路径
urlpatterns = [

  # http://localhost:8000/music/
  url(r'^$',index_views),

  # http://localhost:8000/music/index
  url(r'^index/$',index_views),

  # http://localhost:8000/music/test
  url(r'^test/$',test01_views),

  #http://localhost:8000/music/test/四位数字
  url(r'^test/(\d{4})/$',test02_views),

]