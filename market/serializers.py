from decimal import Decimal

from rest_framework import serializers

from market.models import Product, ProductCategory, ProductStatus, Review
from market.models.product_provider import ProductProvider


class ProductStatusSerializer(serializers.ModelSerializer):
    """Serializer for Product Status model"""

    class Meta:
        model = ProductStatus
        fields = ["id", "name"]


class ProductCategorySerializer(serializers.ModelSerializer):
    """Serializer for Product Category model"""

    class Meta:
        model = ProductCategory
        fields = ["id", "name", "parent_id"]


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "price",
            "price_with_tax",
            "status",
            "category",
        ]

    price_with_tax = serializers.SerializerMethodField(method_name="calculate_tax")

    @staticmethod
    def calculate_tax(product: Product) -> Decimal:
        return product.price * Decimal(1.08)


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Product model"""

    def create(self, validated_data):
        product_id = self.context["product_id"]
        return Review.objects.create(**validated_data, product_id=product_id)

    class Meta:
        model = Review
        fields = ["id", "date", "name", "description"]


class ProductProviderSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = ProductProvider
        fields = ["id", "user_id", "phone", "description"]
