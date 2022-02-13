from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=32, unique=True)
    description = models.TextField(blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='products_mages', blank=True, null=True)
    text = models.TextField(max_length=128)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

