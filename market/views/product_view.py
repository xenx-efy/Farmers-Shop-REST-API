from rest_framework.viewsets import ModelViewSet

from market.models import Product
from market.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.select_related("category").all()
    serializer_class = ProductSerializer

    def get_serializer_context(self):
        return {"request": self.request}
