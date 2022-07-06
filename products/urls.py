from django.urls import path, include
from rest_framework.routers import SimpleRouter

from products.views import ProductViewSet, ProductStatusViewSet, ProductCategoryViewSet

router = SimpleRouter()
router.register(r'products', ProductViewSet, 'product')
router.register(r'products-statuses', ProductStatusViewSet)
router.register(r'products-categories', ProductCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]