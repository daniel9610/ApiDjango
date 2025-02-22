"""ApiDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from ApiDjango import views
from rest_framework import routers
from Clients import views as clients_views 
from Products import views as products_views
from Bills import views as bills_views 
from Bills_Products import views as bills_products_views 

router = routers.SimpleRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'bills', views.BillViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'bills-products', views.Bills_ProductsViewSet)

# router.register(r'bills', views.BillViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('clients-csv/', clients_views.CSV, name ='clients-csv'),
    path('products-csv/', products_views.CSV, name ='products-csv'),
    path('bills-csv/', bills_views.CSV, name ='bills-csv'),
    path('bills-products-csv/', bills_products_views.CSV, name ='bills-products-csv')


]

#### agregar todo lo referente a restframework en el resto de modelos (serilizable, view, )