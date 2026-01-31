from django.urls import path
from . import views

urlpatterns = [

    path('cart-view/', views.cart_view, name='CartItems'),
    path('add-to-cart/<int:product_id>', views.add_to_cart, name='AddToCart'),
    path('remove-cart-item/<int:id>', views.remove_cart_item, name='RemoveFromCart'),

]
