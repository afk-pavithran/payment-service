from .models import ProductDetail, TransactionDetails
from .serializers import ProductSerializer, TransactionSerializer
from restapi.payumoney import PayuMoney
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt
import hashlib
from random import randint

# Create your views here.

# def paymentPayload(request):
#     pass

class Products(APIView):
    def get(self, request, format=None):
        product = ProductDetail.objects.all()
        serialzer = ProductSerializer(product, many=True)
        return Response(serialzer.data)
    pass

class PaymentPayload(APIView):
    KEY = 'JPM7Fg'
    SALT= 'eCwWELxi'
    def get(self, request, format=None):
        return Response("Get Method Done")
    
    
    @csrf_exempt
    def post(self, request, format=None):
        req = request.data
        hash_obj = hashlib.sha256(f"{randint(0,20)}".encode('utf-8'))
        txnid = hash_obj.hexdigest()[0:20]
        req['key'] = 'JPM7Fg'
        req['salt'] = 'TuxqAugd'
        req['txnid'] = txnid
        hash = PayuMoney.generateHash(req)
        payload = {
            'data' : request.data,
            'hash': hash,
            'txnid': txnid
        }
        return Response(payload)


class ResponseRedirect(APIView):

    def get(self, request, format=None):
        d = TransactionDetails.objects.all()
        serializer = TransactionSerializer(d, many=True)
        print(serializer)
        return Response(serializer.data)


    @csrf_exempt
    def post(self, request, format=None):
        # return Response('Payment failed or success')
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        print(serializer.data)
        txn = serializer.data["txnid"]
        return redirect(f"http://localhost:3000/payment-status/{txn}/")

