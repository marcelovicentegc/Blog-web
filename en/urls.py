from django.urls import re_path
from en.views import IndexView, BlogListView, BlogDetailView
from django.views.generic import ListView
from en.models import PostModel

urlpatterns = [
    re_path(r'^$', IndexView.as_view()),  
    re_path(r'^blog/$', BlogListView.as_view()),
    re_path(r'^blog/(?P<slug>[\w\-]+)/$', BlogDetailView.as_view()),
] 