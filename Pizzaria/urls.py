from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import re_path
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("Home.urls")),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
]
