from django.conf.urls import include
from django.urls import re_path
from home.views import IndexView

urlpatterns = [
    re_path(r'^$', IndexView.as_view())
]