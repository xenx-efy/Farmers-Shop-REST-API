from django.db import models


class ProductStatus(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'product status'
        verbose_name_plural = 'product statuses'
