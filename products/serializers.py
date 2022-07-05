from decimal import Decimal

from rest_framework import serializers

from products.models import Product, ProductStatus, ProductCategory


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
