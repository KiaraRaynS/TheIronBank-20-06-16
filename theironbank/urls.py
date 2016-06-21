from django.conf.urls import url, include
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.contrib import admin
from appironbank.views import ViewIndex, SignUpView, ViewUserdata, TransactionInfo, TransactionSend

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ViewIndex.as_view(), name='index'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^logout/$', logout, name='logout'),
    url(r'^makeuser/$', SignUpView.as_view(model=User, ), name='register'),
    url(r'^accounts/profile/$', ViewUserdata.as_view(), name='userdata'),
    url(r'^transaction/(?P<pk>\w+)/$', TransactionInfo.as_view(), name='transactioninfo'),
    url(r'^transfer/$', TransactionSend.as_view(), name='transactiontransfer')
]
