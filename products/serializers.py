from decimal import Decimal

from rest_framework import serializers

from products.models import Product, ProductStatus, ProductCategory, Review


class ProductStatusSerializer(serializers.ModelSerializer):
    """Serializer for Product Status model"""

    class Meta:
        model = ProductStatus
        fields = ['id', 'name']


class ProductCategorySerializer(serializers.ModelSerializer):
    """Serializer for Product Category model"""

    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'parent_id']


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'price_with_tax', 'status', 'category']

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    @staticmethod
    def calculate_tax(product: Product) -> Decimal:
        return product.price * Decimal(1.08)


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""

    class Meta:
        model = Review
        fields = ['id', 'date', 'name', 'description', 'product']
