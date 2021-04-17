from rest_framework import serializers
from .models import ProductDetail, TransactionDetails

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetails
        fields = ['txnid', 'mihpayid', 'amount', 'status', 'email', 'payment_source']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        fields = ['name', 'price', 'quantity']