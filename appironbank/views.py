from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


class ViewIndex(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/profile/'


class ViewUserdata(TemplateView):
    template_name = 'userdetail.html'
