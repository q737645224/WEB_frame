from django.conf.urls import url
from .views import *
urlpatterns = [
  #访问路径是http://localhost:8000/news/,交给index_views去处理
  url(r'^$',index_views),
]