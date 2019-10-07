from django.db import models

# Create your models here.
class Client(models.Model):
    document = models.CharField(max_length=15)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(
        'email address',
        max_length=50,
        unique = True,
        error_messages = {
            'unique':'A user with that email already exist.'
        }
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)