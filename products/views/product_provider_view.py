from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models.product_provider import ProductProvider
from products.serializers import ProductProviderSerializer
from rest_framework.decorators import action


class ProductProviderViewSet(ModelViewSet):
    queryset = ProductProvider.objects.all()
    serializer_class = ProductProviderSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False)
    def me(self, request):
        product_provider, created = ProductProvider.objects.get_or_create(user_id=request.user.id)

        if request.method == 'GET':
            serializer = ProductProviderSerializer(product_provider)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProductProviderSerializer(product_provider, request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

    def get_serializer_context(self):
        return {'request': self.request}
