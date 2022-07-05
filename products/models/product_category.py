from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    parent_id = models.PositiveBigIntegerField(blank=True)
