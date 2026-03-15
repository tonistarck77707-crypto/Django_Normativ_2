from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # store app
    path('products/', include('store.urls')),

    # posts app
    path('posts/', include('posts.urls')),

    # bo‘sh path → products sahifasiga yo‘naltirish
    path('', RedirectView.as_view(url='/products/')),
]