from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from products.models import ProductStatus
from products.serializers import ProductStatusSerializer


@api_view(http_method_names=['GET'])
def product_status_list(request):
    queryset = ProductStatus.objects.all()
    serializer = ProductStatusSerializer(queryset, many=True)

    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def product_status_detail(request, pk):
    product_status = get_object_or_404(ProductStatus, pk=pk)
    serializer = ProductStatusSerializer(product_status)

    return Response(serializer.data)
