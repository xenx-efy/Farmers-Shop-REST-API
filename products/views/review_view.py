from rest_framework.viewsets import ModelViewSet

from products.models import Review
from products.serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        if self.kwargs.get('product_pk') is not None:
            return {'product_id': self.kwargs['product_pk']}
