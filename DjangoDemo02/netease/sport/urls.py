from django.conf.urls import url
from .views import *

urlpatterns = [
  #访问路径是http://localhost:8000/sport/
  url(r'^$',index_views),
]