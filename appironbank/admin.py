from django.contrib import admin
from appironbank.models import Transaction

# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'balancemod', 'transtype']

admin.site.register(Transaction, TransactionAdmin)
