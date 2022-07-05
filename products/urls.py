from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='products-list'),
    path('products/<int:id>/', views.ProductDetail.as_view(), name='product-detail'),

    path('products-statuses/', views.product_status_list, name='products-statuses-list'),
    path('products-statuses/<int:pk>/', views.product_status_detail, name='product-status-detail'),

    path('products-categories/', views.product_category_list, name='products-categories-list'),
    path('products-categories/<int:pk>', views.product_category_detail, name='product-category-detail'),
]
