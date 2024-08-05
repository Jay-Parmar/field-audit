from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=255)
    transaction_cursor = models.CharField(null=True, max_length=255)
    bank_name = models.CharField(null=True, max_length=255)
    is_active = models.BooleanField(default=True)


class Account(models.Model):
    name = models.CharField(null=True, max_length=255)
    item = models.ForeignKey(Item, on_delete=models.DO_NOTHING)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    category = models.CharField(null=True, max_length=255)
    date = models.DateField(null=True)
    authorized_date = models.DateField(null=True)
    name = models.CharField(null=True, max_length=255)
    amount = models.FloatField(null=True)
    currency_code = models.CharField(null=True, max_length=255)
    is_removed = models.BooleanField(default=False)


