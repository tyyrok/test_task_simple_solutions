from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField()
    description = models.TextField()
