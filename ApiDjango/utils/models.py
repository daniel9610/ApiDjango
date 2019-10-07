"""Django models utilities"""

#Django 
from django.db import models

class ApiDjangoModel(models.Model):
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text = 'Date time on which the object was created.'
    )
    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text = 'Date time on which the object was last modified.'
    )
    class Meta:
        abstract = True
        get_latest_by = 'created'
        ordering = ['-created', '-modified']