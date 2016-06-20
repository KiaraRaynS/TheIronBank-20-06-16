from django.db import models
from django.contrib.auth.models import User

# Create your models here.

choices = (
    ('debit', 'Debit'),
    ('credit', 'Credit'),
    )


class Transaction(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    balancemod = models.IntegerField()
    user = models.ForeignKey(User)
    transtype = models.CharField(max_length=10, choices=choices)
