from django.urls import path
from . import views

urlpatterns = [

    path("", views.landing_page, name="landing_page"),
    path("product/", views.product, name="product"),
    path("manage-products/", views.manage_product, name="manage_products"),
    path("create-product/", views.create_product, name="create_product"),
    path('delete-product/<int:product_id>/', views.delete_product, name="delete_product"),
    path('update-product/<int:product_id>/', views.update_product, name="update_product"),
    path('category/', views.category, name="category"),
    path('category-products/<int:category_id>', views.category_products, name="category_products"),
]
