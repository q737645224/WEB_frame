from django.conf.urls import url
from .views import *
urlpatterns = [
  #访问路径是http://localhost:8000/
  url(r'^$',index_views),

  #访问路径是http://localhost:8000/login/
  url(r'^login$',login_views),

  #访问路径是http://localhost:8000/register/
  url(r'^register/$',register_views),
]