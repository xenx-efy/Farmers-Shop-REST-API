from decimal import Decimal

from rest_framework import serializers

from products.models import Product, ProductStatus, ProductCategory


class ProductStatusSerializer(serializers.Serializer):
    """Serializer for Product Status model"""

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=250)


class ProductCategorySerializer(serializers.Serializer):
    """Serializer for Product Category model"""

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=250)
    parent_id = serializers.IntegerField()


class ProductSerializer(serializers.Serializer):
    """Serializer for Product model"""

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)
    description = serializers.CharField()
    unit_price = serializers.IntegerField(source='price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    status = serializers.HyperlinkedRelatedField(
        queryset=ProductStatus.objects.all(),
        view_name='product-status-detail'
    )
    category = serializers.HyperlinkedRelatedField(
        queryset=ProductCategory.objects.all(),
        view_name='product-category-detail'
    )

    @staticmethod
    def calculate_tax(product: Product) -> Decimal:
        return product.price * Decimal(1.08)
