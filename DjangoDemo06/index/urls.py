from django.conf.urls import url
from .views import *
urlpatterns = [
  url(r'^01-request/$',request_views),
  url(r'^02-request/$',request02_views),
  url(r'^03-post/$',post_views),
  url(r'^04-all/$',all_views),
  url(r'^05-register/$',register_views),
  url(r'^06-form/$',form_views),
]

urlpatterns += [
  url(r'^07-form-register/$',form_register),
  url(r'^08-widget1/$',widget1_views),
  url(r'^09-widget2/$',widget2_views),
  url(r'^10-setCookie/$',setcookie_views),
  url(r'^11-getCookie/$',getcookie_views),
]

urlpatterns += [
  url(r'^12-ajax/$',ajax_views),
  url(r'^12-server/$',server12_views),
  url(r'^13-ajax-post/$',ajax_post),
  url(r'^13-server/$',server13_views),
]