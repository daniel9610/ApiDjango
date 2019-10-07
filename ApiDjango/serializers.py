from rest_framework import serializers
from Clients.models import Client
from Products.models import Product
from Bills.models import Bill
from Bills_Products.models import Bills_Products

class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'document', 'first_name', 'last_name', 'email', 'created_at', 'updated_at']

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class BillSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bill
        fields = ['id', 'client_id', 'company_name', 'nit', 'code', 'created_at', 'updated_at']

class BillsProductsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Bills_Products
        fields = ['id', 'bill_id', 'product_id']