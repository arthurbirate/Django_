from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('products/', views.getProducts),
    path('product/<int:product_id>', views.getProduct)

]
