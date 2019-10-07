from django.shortcuts import render
from rest_framework import viewsets
from ApiDjango.serializers import ClientSerializer, ProductSerializer, BillSerializer, BillsProductsSerializer
from Clients.models import Client
from Products.models import Product
from Bills.models import Bill
from Bills_Products.models import Bills_Products

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class BillViewSet(viewsets.ModelViewSet):

    queryset = Bill.objects.all()
    serializer_class = BillSerializer

class Bills_ProductsViewSet(viewsets.ModelViewSet):

    queryset = Bills_Products.objects.all()
    serializer_class = BillsProductsSerializer
