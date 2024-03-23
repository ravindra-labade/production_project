from django.urls import path
from .views import add_product, show_product, update_product, cancel_product


urlpatterns = [
    path('add/', add_product, name='add_url'),
    path('show/', show_product, name='show_url'),
    path('update/<int:pk>/', update_product, name='update_url'),
    path('cancel/<int:pk>/', cancel_product, name='cancel_url'),
]


