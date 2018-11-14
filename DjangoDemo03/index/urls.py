from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'01-parent/&',parent_views),
    url(r'login/$', login_views,name="LG"),
    url(r'register/$', register_views,name="RG")
]
