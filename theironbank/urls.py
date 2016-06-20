from django.conf.urls import url
from django.contrib import admin
from appironbank.views import ViewIndex

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ViewIndex.as_view(), name='index')
]
