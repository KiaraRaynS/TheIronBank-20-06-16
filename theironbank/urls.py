from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib import admin
from appironbank.views import ViewIndex, SignUpView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ViewIndex.as_view(), name='index'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^makeuser/$', SignUpView.as_view(model=User))
]
