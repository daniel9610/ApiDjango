from django.db import models
from Products.models import Product
from Bills.models import Bill

# Create your models here.
class Bills_Products(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)