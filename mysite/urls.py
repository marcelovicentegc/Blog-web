from django.contrib import admin
from django.urls import include, path, re_path




urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('home.urls')),
    re_path(r'^en/', include('en.urls')),
    re_path(r'^pt-br/', include('ptbr.urls')),
]
