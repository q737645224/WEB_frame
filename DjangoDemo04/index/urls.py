from django.conf.urls import url
from .views import *
urlpatterns = [
  url(r'^01-request/$',request_views),
  url(r'^02-get/$',get_views),
  url(r'^03-post/$',post_views),
  url(r'^04-form/$',form_views),
]

urlpatterns = [
  url(r'^05-register/$',register_views),
  url(r'^06-login/$',login_views),
  url(r'^07-setCookie/$',setCookie_views),
  url(r'^08-getCookie/$',getCookie_views),
  url(r'^09-login/$',login09_views),
  url(r'^10-setSession/$',setSession_views),
  url(r'^11-getSession/$',getSession_views),
]