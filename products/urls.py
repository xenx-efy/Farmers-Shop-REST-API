from django.contrib import admin
from django.urls import path

from products import views

urlpatterns = [
    path('', views.product_list),
    path('<int:id>/', views.product_detail),
]
