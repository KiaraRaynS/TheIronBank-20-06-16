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

    def get_absolute_url(self):
        user = self.request.user
        return reverse(ViewProfile, args=[user.id])


class ViewProfile(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        user = self.kwargs['pk']
        context['user'] = User.objects.get(id=user)
        return context


class ViewUserdata(TemplateView):
    template_name = 'userdetail.html'
