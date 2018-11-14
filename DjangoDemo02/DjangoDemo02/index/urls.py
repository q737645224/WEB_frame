from django.conf.urls import url
from .views import *

urlpatterns = [
  #访问路径:http://localhost:8000/01-temp
  url(r'^01-temp/$',temp_views),
  #访问路径:http://localhost:8000/02-var
  url(r'^02-var/$',var_views),
  #访问路径:http://localhost:8000/03-static
  url(r'^03-static/$',static_views),
]