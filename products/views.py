from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


@api_view(http_method_names=['GET'])
def product_list(request):
    return Response('ok')


@api_view(http_method_names=['GET'])
def product_detail(request, id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product)

    return Response(serializer.data)
