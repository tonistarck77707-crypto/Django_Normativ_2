from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hush kelindigiz Saytga!")

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),  # admin import qilindi
    path('products/', include('store.urls')),
]