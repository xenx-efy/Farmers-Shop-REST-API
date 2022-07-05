from django.contrib import admin

from .models import Product, ProductCategory, ProductStatus


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductStatus)
class ProductStatusAdmin(admin.ModelAdmin):
    pass
