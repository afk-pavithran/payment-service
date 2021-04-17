from django.db import models

# Create your models here.

class TransactionDetails(models.Model):
    txnid = models.CharField(max_length=50)
    mihpayid = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    payment_source = models.CharField(max_length=50)


class ProductDetail(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()