from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from products.models import Product


@api_view(['GET'])
def getRoutes(request):
    routes = [

        {'GET': 'api/products'},
        {'GET': 'api/products/id'},
        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},

    ]

    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, product_id):
    product = Product.objects.get(id=product_id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
