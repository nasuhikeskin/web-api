from rest_framework import serializers

from .models import Product
from .models import Package

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'genislik', 'uzunluk', 'yukseklik', 'agirlik')

class PackageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Package
        fields = ('package_type', 'product_id', )
