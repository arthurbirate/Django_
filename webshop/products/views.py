from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import escape_leading_slashes

from .models import Product, Category, SubCategory
from .forms import ProductForm


# Create your views here.
def category(request):
    categories = Category.objects.all()
    return render(request, "products/category.html", {"categories": categories})


def products(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {"products": products})


def product(request):
    return HttpResponse("Hello, this is a single product page.")


def manage_product(request):
    products = Product.objects.all().order_by("stock")

    for product in products:
        if product.is_sold_out:
            product.display_stock = "Sold Out"
            product.stock_class = "text-red-600"
        else:
            product.display_stock = "In stock"
    return render(request, "products/manage-products.html", {"products": products})


def create_product(request):
    form = ProductForm()
    if request.method == "POST":

        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("manage_products")

    context = {'form': form}
    return render(request, "products/product_form.html", context)


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)

    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("manage_products")
    context = {'form': form}
    return render(request, "products/product_form.html", context)


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {'product': product}

    if request.method == "POST":
        product.delete()
        return redirect("manage_products")

    return render(request, "products/delete-product.html", context)


def category_products(request, category_id):
    category_ = Category.objects.get(id=category_id)
    subcategories = SubCategory.objects.filter(category=category_)
    products_ = Product.objects.filter(sub_category__in=subcategories)

    context = {'products': products_, 'category': category_, 'subcategories': subcategories}

    return render(request, "products/category_products.html", context)
