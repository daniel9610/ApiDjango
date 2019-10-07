from django.shortcuts import render
from Clients.models import Client
import csv
from django.http import HttpResponse
# Create your views here.



def CSV(request):
    # The only line to customize
    model_class = Client

    meta = model_class._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in model_class.objects.all():
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response