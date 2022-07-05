from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from products.models import ProductCategory
from products.serializers import ProductCategorySerializer


@api_view(http_method_names=['GET'])
def product_category_list(request):
    queryset = ProductCategory.objects.all()
    serializer = ProductCategorySerializer(queryset, many=True)

    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def product_category_detail(request, pk):
    product_category = get_object_or_404(ProductCategory, pk=pk)
    serializer = ProductCategorySerializer(product_category)

    return Response(serializer.data)
