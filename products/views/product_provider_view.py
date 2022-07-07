from rest_framework.viewsets import ModelViewSet

from products.models.product_provider import ProductProvider
from products.serializers import ProductProviderSerializer


class ProductProviderViewSet(ModelViewSet):
    queryset = ProductProvider.objects.all()
    serializer_class = ProductProviderSerializer

    def get_serializer_context(self):
        return {'request': self.request}
