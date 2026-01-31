from itertools import product

from django.shortcuts import render, redirect
from .models import CartItems
from products.models import Product


# Create your views here.

def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        cart_item, created = CartItems.objects.get_or_create(product=product)
        cart_item.quantity += 1
        cart_item.save()
        return redirect("CartItems")
    return None


def cart_view(request):
    cart_items = CartItems.objects.all()
    subtotal = 0
    for item in cart_items:
        price = item.total_price
        subtotal += price

    total_price = subtotal

    context = {"cartItems": cart_items, "total_price": total_price}
    return render(request, "CartModule/cart-view.html", context)


def remove_cart_item(request, id):
    cart_item_product = CartItems.objects.get(product=id)
    if cart_item_product.quantity > 1:
        cart_item_product.quantity -= 1
        cart_item_product.save()
    else:
        cart_item_product.delete()

    return redirect("CartItems")
