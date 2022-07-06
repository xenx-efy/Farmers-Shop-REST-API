from rest_framework.viewsets import ModelViewSet

from products.models import ProductStatus
from products.serializers import ProductStatusSerializer


class ProductStatusViewSet(ModelViewSet):
    queryset = ProductStatus.objects.all()
    serializer_class = ProductStatusSerializer

    def get_serializer_context(self):
        return {'request': self.request}
