from django.db import models


class Product(models.Model):
    category = models.ForeignKey("products.ProductCategory", on_delete=models.SET_NULL, blank=True, null=True)
    status = models.ForeignKey("products.ProductStatus", on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    owner = models.ForeignKey("products.ProductProvider", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Model string representation for admin panel"""
        return self.title

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"
