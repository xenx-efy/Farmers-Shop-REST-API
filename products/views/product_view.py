from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.views import APIView


class ProductList(APIView):
    def get(self, request):
        queryset = Product.objects.select_related('category').all()
        serializer = ProductSerializer(queryset, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)

        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
