from rest_framework.viewsets import ModelViewSet

from products.models import Product, Review
from products.serializers import ProductSerializer, ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_serializer_context(self):
        return {'request': self.request}
