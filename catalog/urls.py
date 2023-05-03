from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, home, contacts


app_name = CatalogConfig.name

urlpatterns = [
    path('', index),
    path('home/', home),
    path('contacts/', contacts),
]