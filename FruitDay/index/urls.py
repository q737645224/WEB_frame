from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^cart/$',cart_views),
    url(r'^login/$',login_views,name='login'),
    url(r'^register/$',register_views,name='register'),
    url(r'^check_login/$',check_login),
    url(r'^logout/$',logout_views),
    url(r'^check_repetion/$',check_repetion),
    url(r'^load_type_goods/$',load_type_goods),
    url(r'^$',index_views),
]