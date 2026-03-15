from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),           # bo‘sh path (http://127.0.0.1:8000/products/)
    path('list/', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/edit/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
]