
from django.db import models
from .account import Account

class Transaction(models.Model):
    id              =models.AutoField(primary_key=True)
    origin_account  =models.ForeignKey(Account, related_name="origin", on_delete=models.CASCADE)
    destiny_account =models.ForeignKey(Account, related_name="destiny", on_delete=models.CASCADE)
    amount          =models.IntegerField(default=True)
    register_date   =models.DateField(auto_now_add=True, blank=True)
    note            =models.CharField(max_length=100)