from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=60)
    genislik = models.DecimalField(max_digits=5, decimal_places=2)
    yukseklik = models.DecimalField(max_digits=5, decimal_places=2)
    agirlik = models.DecimalField(max_digits=5, decimal_places=2)
    uzunluk = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name


class Package(models.Model):
    package_type = models.CharField(max_length=60)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.package_type