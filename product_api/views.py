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
def product_list(request): # renvoie la liste complète des produits ordonnée par nom du produit
    if request.method == 'GET':
        products = Product.objects.all().order_by('name')
        productSerializer =  ProductSerializer(products, many = True)
        return Response(productSerializer.data)
    elif request.method == 'POST':
        pass
        # prodSerialize = ProductSerializer(data = request.data)
        # if prodSerialize.is_valid():
        #     prodSerialize.save()
        #     return Response(prodSerialize.data, status = 201)
        # return JsonResponse(prodSerialize.errors, status = 400)



@api_view(['GET'])
def product_select(request, name): #revoie le produit avec le nom 'name', sinon renvoie message d'erreur
    try:
        product = Product.objects.get(name=name)
    except Product.DoesNotExist:
        return Response({"message":"Product not available...", "data": []}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        productSerializer =  ProductSerializer(product)
        return Response({"message" :"request sent successfully", "data": productSerializer.data}, status = status.HTTP_200_OK)

@api_view(['GET'])
def product_rayon(request, rayon): #renvoie les produits appartement au rayon 'rayon' ordonnées par nom du produit, sinon renvoie message d'erreur
    try:
        product = Product.objects.get(rayon = rayon)
    except Product.DoesNotExist:
        return Response({"message":"No products available in this current rayon...", "data": []}, status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        productSerializer =  ProductSerializer(product, many=True)
        return Response({"message" :"request sent successfully", "data": productSerializer.data}, status = status.HTTP_200_OK)

@api_view(['POST'])
def product_prix(request): # renvoie les produits appartenant à l'intervall de prix (min, max) prdonnée par prix, sinon renvoi message d'erreur
    min = request.data.get('min')
    max = request.data.get('max')
    if min == None or max == None:
        return Response("request fields error...", status=status.HTTP_400_BAD_REQUEST)
    product = Product.objects.filter(prix__gte = min, prix__lte = max).order_by('prix')
    if request.method == 'POST':
        productSerializer =  ProductSerializer(product, many = True)
        if len(product) == 0: 
            return Response({"message": "No products available in this range of prices....", "data": productSerializer.data}  , status = status.HTTP_404_NOT_FOUND)
        return Response({"message" :"request sent successfully", "data": productSerializer.data}, status = status.HTTP_200_OK)

    