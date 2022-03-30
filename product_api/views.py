from this import d
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from product_api.models import Product
from product_api.serializers import ProductSerializer

def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        productSerializer =  ProductSerializer(products, many = True)
        return JsonResponse(productSerializer.data, safe = False)
    elif request.method == 'POST':
        pass
        # data = JSONParser().parse(request)
        # prodSerialize = ProductSerializer(data = data)

        # if prodSerialize.is_valid():
        #     prodSerialize.save()
        #     return JsonResponse(prodSerialize.data, status = 201)
        # return JsonResponse(prodSerialize.errors, status = 400)
