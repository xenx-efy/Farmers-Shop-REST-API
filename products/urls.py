from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from products.views import (
    ProductCategoryViewSet,
    ProductProviderViewSet,
    ProductStatusViewSet,
    ProductViewSet,
    ReviewViewSet,
)

router = DefaultRouter()
router.register(r"products", ProductViewSet, "product")
router.register(r"products-statuses", ProductStatusViewSet)
router.register(r"products-categories", ProductCategoryViewSet)
router.register(r"products-providers", ProductProviderViewSet)

products_router = routers.NestedDefaultRouter(router, "products", lookup="product")
products_router.register(r"reviews", ReviewViewSet, basename="product-reviews")

urlpatterns = router.urls + products_router.urls
