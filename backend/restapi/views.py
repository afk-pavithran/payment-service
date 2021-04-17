from restapi.payumoney import PayuMoney
from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# def paymentPayload(request):
#     pass

class PaymentPayload(APIView):
    KEY = 'JPM7Fg'
    SALT= 'eCwWELxi'
    def get(self, request, format=None):
        return Response("Get Method Done")

    def post(self, request, format=None):
        hash = PayuMoney.generateHash(request.data)
        payload = {
            'data' : request.data,
            'hash': hash,
        }
        return Response(payload)


class ResponseRedirect(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        # return Response('Payment failed or success')
        print(request.data)
        return redirect('http://localhost:3000/payment-status/')