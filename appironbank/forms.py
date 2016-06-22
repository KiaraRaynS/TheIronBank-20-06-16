from django.forms import ModelForm
from django import forms
from appironbank.models import Transaction


class TransactionForm(ModelForm):
    sendto = forms.IntegerField()

    class Meta:
        model = Transaction
        fields = ['balancemod', 'sendto']
