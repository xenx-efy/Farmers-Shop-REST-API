from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    parent_id = models.PositiveBigIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        """Model string representation for admin panel"""
        return self.name

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'
