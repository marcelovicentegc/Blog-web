from django.contrib import admin
from django.urls import include, path, re_path




urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('home.urls')),
    re_path(r'^en/', include('en.urls')),
    re_path(r'^pt-br/', include('ptbr.urls')),
]


# Comment out or delete these lines in production
from mysite.settings import dev
from django.conf.urls import handler404, handler500
from mysite.views import Error400, Error403, Error404, Error500
from django.views.static import serve

handler400 = Error400.as_view()
handler403 = Error403.as_view()
handler404 = Error404.as_view()
handler500 = Error500.as_view()

if dev.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': dev.MEDIA_ROOT,
        }),
    ]