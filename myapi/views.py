from django.shortcuts import render
from rest_framework import viewsets

from .serializers import ProductSerializer
from .serializers import PackageSerializer
from .models import Product
from .models import Package


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all().order_by('package_type')
    serializer_class = PackageSerializer

# Create your views here.
