from django.urls import path

from . import views

urlpatterns = [
    path('customer-wishlist/<int:customer_id>', views.customer_wishlist, name='customer_wishlist'),
]
