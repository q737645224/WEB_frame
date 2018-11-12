from .views import *
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^index/$', index01),
]