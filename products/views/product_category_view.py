from rest_framework.viewsets import ModelViewSet

from products.models import ProductCategory
from products.serializers import ProductCategorySerializer


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def get_serializer_context(self):
        return {'request': self.request}
