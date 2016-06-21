from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from appironbank.models import Transaction

# Create your views here.


class ViewIndex(TemplateView):
    template_name = 'index.html'


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/accounts/profile/'


class ViewUserdata(CreateView):
    model = Transaction
    fields = ['balancemod', 'transtype']
    success_url = '/accounts/profile/'

    def form_valid(self, form):
        transaction = form.save(commit=False)
        transaction.user = self.request.user
        return super(ViewUserdata, self).form_valid(form)

    def get_context_data(self, **kwargs):
        user = self.request.user
        kwargs['transactions'] = Transaction.objects.filter(user=user)
        return super(ViewUserdata, self).get_context_data(**kwargs)


class TransactionInfo(TemplateView):
    template_name = 'transdata.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transaction_id = self.kwargs['pk']
        context['transaction'] = Transaction.objects.get(id=transaction_id)
        return context
