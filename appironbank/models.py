from django.db import models
from django.contrib.auth.models import User

# Create your models here.

choices = (
    ('debit', 'Debit'),
    ('credit', 'Credit'),
    )


class Transaction(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    balancemod = models.PositiveIntegerField()
    user = models.ForeignKey(User, related_name='currentuser')
    transtype = models.CharField(max_length=10, choices=choices)
    senduser = models.ForeignKey(User, null=True, related_name='senduser')
