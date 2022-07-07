from django.db import models


class ProductStatus(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        """Model string representation for admin panel"""
        return self.name

    class Meta:
        verbose_name = "product status"
        verbose_name_plural = "product statuses"
