from django.contrib import admin

from .models import Product, ProductCategory, ProductStatus


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'parent_id']


@admin.register(ProductStatus)
class ProductStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
