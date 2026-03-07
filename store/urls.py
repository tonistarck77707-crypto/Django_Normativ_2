from django.urls import path
from .views import register_view, login_view
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_create, name='product_create'),
    path('<int:pk>/update/', views.product_update, name='product_update'),
    path('<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]