from django.conf.urls import url, include
from django.contrib import admin
from appironbank.views import ViewIndex

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ViewIndex.as_view(), name='index'),
    url(r'^', include('django.contrib.auth.urls')),
]
