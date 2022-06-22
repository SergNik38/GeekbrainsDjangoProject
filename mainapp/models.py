from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    date = models.DateField()
    price = models.IntegerField()
    unit = models.CharField(max_length=64)
    provider = models.CharField(max_length=64)
