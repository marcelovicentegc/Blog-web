from django.urls import re_path
from en.views import IndexView, BlogListView, BlogDetailView

urlpatterns = [
    re_path(r'^$', IndexView.as_view()),  
    re_path(r'^blog/$', BlogListView.as_view()),
    re_path(r'^blog/(?P<slug>[\w\-]+)/$', BlogDetailView.as_view()),
] 
