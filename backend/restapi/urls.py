from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic.base import RedirectView
from rest_framework import routers
from .views import PaymentPayload, Products, ResponseRedirect

# router = routers.DefaultRouter()
# router.register(r'payload', PaymentPayload.as_view(), basename='payload')

urlpatterns = [
    path('payload/', PaymentPayload.as_view()),
    path('response/', ResponseRedirect.as_view()),
    path('prod/', Products.as_view())
]