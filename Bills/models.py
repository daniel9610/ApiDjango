from django.db import models
from Clients.models import Client

# Create your models here.
class Bill(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=45)
    nit = models.CharField(max_length=45)
    code = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

