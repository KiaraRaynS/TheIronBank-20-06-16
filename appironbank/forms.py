from django.forms import ModelForm
from django import forms
from appironbank.models import Transaction


class TransactionForm(ModelForm):
    sendto = forms.IntegerField()
    error = forms.CharField(max_length=50)

    class Meta:
        model = Transaction
        fields = ['balancemod', 'sendto']
