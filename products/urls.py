from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path('products/', views.product_list, name='products-list'),
    path('products/<int:pk>/', views.product_detail, name='product-detail'),

    path('products-statuses/', views.product_status_list, name='products-statuses-list'),
    path('products-statuses/<int:pk>/', views.product_status_detail, name='product-status-detail'),

    path('products-categories/', views.product_category_list, name='products-categories-list'),
    path('products-categories/<int:pk>', views.product_category_detail, name='product-category-detail'),
]
