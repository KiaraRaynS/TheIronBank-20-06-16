import datetime
from appironbank.forms import TransactionForm
from django.db.models import Sum
from django.core.exceptions import ValidationError
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
    balance = 0

    def form_valid(self, form):
        balance = Transaction.objects.filter(user=self.request.user).aggregate(Sum('balancemod'))
        transaction = form.save(commit=False)
        if transaction.transtype == 'debit':
            transaction.balancemod = -transaction.balancemod
            if balance['balancemod__sum']+transaction.balancemod < 0:
                raise ValidationError("Insufficient Funds")
        else:
            transaction.balancemod = transaction.balancemod
        transaction.user = self.request.user

        return super(ViewUserdata, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        cutoffdate = datetime.datetime.now() + datetime.timedelta(days=-30)
        context['transactions'] = Transaction.objects.filter(user=user).filter(date__gt=cutoffdate)
        context['balance'] = Transaction.objects.filter(user=user).aggregate(Sum('balancemod'))
        return context


class TransactionSend(CreateView):
    form_class = TransactionForm
    success_url = '/accounts/profile'
    template_name = 'appironbank/transaction_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['balance'] = Transaction.objects.filter(user=user).aggregate(Sum('balancemod'))
        return context

    def form_valid(self, form):
        balance = Transaction.objects.filter(user=self.request.user).aggregate(Sum('balancemod'))
        transaction = form.save(commit=False)

        # for user sending funds
        transaction.balancemod = -transaction.balancemod
        transaction.user = self.request.user
        transaction.transtype = 'debit'
        if balance['balancemod__sum'] + transaction.balancemod < 0:
            raise ValidationError("Insuffecient Funds")
        # credit = recieve money
        # debit = withdrawl

        # for user recieving funds
        sendto = User.objects.get(id=form.cleaned_data['sendto'])
        balancemod = -transaction.balancemod
        transtype = 'credit'
        Transaction.objects.create(user=sendto, balancemod=balancemod, transtype=transtype)

        return super().form_valid(form)


class TransactionInfo(TemplateView):
    template_name = 'transdata.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transaction_id = self.kwargs['pk']
        context['transaction'] = Transaction.objects.get(id=transaction_id)
        return context
