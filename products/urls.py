from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from pprint import pprint

from products.views import ProductViewSet, ProductStatusViewSet, ProductCategoryViewSet

router = SimpleRouter()
router.register(r'products', ProductViewSet, 'product')
router.register(r'products-statuses', ProductStatusViewSet)
router.register(r'products-categories', ProductCategoryViewSet)
# pprint(router.registry)
pprint(router.urls)

urlpatterns = [
    path('', include(router.urls)),
]