from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


@api_view(http_method_names=['GET'])
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)

    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
