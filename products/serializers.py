from decimal import Decimal

from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)
    description = serializers.CharField()
    unit_price = serializers.IntegerField(source='price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    @staticmethod
    def calculate_tax(product: Product) -> Decimal:
        return product.price * Decimal(1.08)
