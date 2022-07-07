from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from products.views import ProductViewSet, ProductStatusViewSet, ProductCategoryViewSet, ReviewViewSet, \
    ProductProviderViewSet

router = DefaultRouter()
router.register('products', ProductViewSet, 'product')
router.register('products-statuses', ProductStatusViewSet)
router.register('products-categories', ProductCategoryViewSet)
router.register('products-providers', ProductProviderViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + products_router.urls
