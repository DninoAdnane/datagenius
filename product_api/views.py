from this import d
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from product_api.models import Product
from product_api.serializers import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        productSerializer =  ProductSerializer(products, many = True)
        return Response(productSerializer.data)
    elif request.method == 'POST':
        pass
        # prodSerialize = ProductSerializer(data = request.data)
        # if prodSerialize.is_valid():
        #     prodSerialize.save()
        #     return Response(prodSerialize.data, status = 201)
        # return JsonResponse(prodSerialize.errors, status = 400)


def product_list_name(request):
    if request.method == 'GET':
        Product.objects.all()

@api_view(['GET'])
def product_select(request, name):
    try:
        product = Product.objects.get(name=name)
    except Product.DoesNotExist:
        return Response("Product not available...", status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        productSerializer =  ProductSerializer(product)
        return Response(productSerializer.data)

@api_view(['GET'])
def product_rayon(request, rayon):
    try:
        product = Product.objects.get(rayon = rayon)
    except Product.DoesNotExist:
        return Response("No products available in this current rayon....", status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        productSerializer =  ProductSerializer(product)
        return Response(productSerializer.data)

@api_view(['POST'])
def product_prix(request):
    try:
        min = request.data.get('min')
        max = request.data.get('max')
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product = Product.objects.filter(prix__gte = min, prix__lte = max)
    if request.method == 'POST':
        productSerializer =  ProductSerializer(product, many = True)
        if len(product) == 0: 
            return Response({"message": "No products available in this range of prices....", "data": productSerializer.data}  , status = status.HTTP_404_NOT_FOUND)
        return Response(productSerializer.data)

    