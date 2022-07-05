from django.db import models


class ProductStatus(models.Model):
    name = models.CharField(max_length=250)
