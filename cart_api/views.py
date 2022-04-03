import django
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from cart_api.models import ShoppingCart, User, ProductCart, Commonde
from product_api.models import Product, Remise
from product_api.enumModels import TypeRemise
from cart_api.serializers import ShoppingCartSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime, timezone

# Create your views here.


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_product_to_chart(request):
    
        usr_code = request.data.get('user')
        product_name = request.data.get('name')
        quantity = request.data.get('count')
        if usr_code is None or product_name is None or quantity is None :
            return Response({"message":"request fields error...", "data": []}, status=status.HTTP_400_BAD_REQUEST)
        try:
            product = Product.objects.get(name = product_name) # voir si le produit exsite
        except Product.DoesNotExist:
            return Response({"message":"Product not availabe...", "data": []}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            user = User.objects.get(code = usr_code)
        except User.DoesNotExist:
            return Response({"message":"Please create an account first...", "data": []}, status=status.HTTP_404_NOT_FOUND)
        
        if product.quantite < quantity:
            return Response({"message":"Insufficient quantity for the product: "+product_name, "data": []}, status=status.HTTP_404_NOT_FOUND)
        else:
            product.quantite = product.quantite - quantity
        try:
            shoppingCart = ShoppingCart.objects.get(user=user, validated = False) # one recupère le shopping cart qui contiendra les productCart si l'utilisateur avait déjà commencer à acheter
        except ShoppingCart.DoesNotExist:
            shoppingCart = ShoppingCart(user=user) # Sinon, on crée un shopping cart
        
        remises = Remise.objects.filter(product=product) # les remise associés au produit
        totalPrix = product.prix * quantity # cout totale
        prixRemise = 0
        for remise in remises:
            if remise.typeRemise == TypeRemise.OFFRE and quantity >= remise.nbAchete: # On offre au client un nombre de produit si il ya l'offre et si il a pri le bon nombre de produit
                if product.quantite < remise.nbOffer:
                    quantity = quantity + product.quantite # Si il n'y a pas suffisement, on donne le reste
                    product.quantite = 0
                else:
                    product.quantite = product.quantite - remise.nbOffer
                    quantity = quantity + remise.nbOffer
            elif remise.typeRemise == TypeRemise.REDUCTION: # On applique une réduction du prix
                prixRemise = (totalPrix * remise.tauxRed)/100
        product.save()
        shoppingCart.save() #containdra les produits acheté par l'utilisateur
        productCart = ProductCart(product = product, quantity = quantity, prix = totalPrix, remisePrix = prixRemise, finalPrix = (totalPrix-prixRemise), cart = shoppingCart) # ajout du produit
        productCart.save()
        return Response({"message" :"Product added successfully", "data": []}, status = status.HTTP_202_ACCEPTED)
        

@api_view(['POST'])
def validate_cart(request):
    if request.method == 'POST':
        usr_code = request.data.get('user')
        if usr_code is None:
            return Response({"message":"request fields error...", "data": []}, status=status.HTTP_400_BAD_REQUEST)

        try:
           user = User.objects.get(code = usr_code) 
        except User.DoesNotExist:
            return Response({"message":"Please create an account first...", "data": []}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            shoppingCart =  ShoppingCart.objects.get(user = user, validated = False) # Validated == False veut dire qu'il ya un shopping cart current, et que l'utilisateur n'a pas encore annuler ou passer la commande
        except ShoppingCart.DoesNotExist:
            return Response({"message":"No current shopping cart...", "data": []}, status=status.HTTP_404_NOT_FOUND)
        
        try: # Permet de vérifier si l'utilisateur avait déjà effectué une commende dans les 60 secondes précédentes
            command = Commonde.objects.filter(user = user).latest('date')
            difference = datetime.now(timezone.utc) - command.date
            if (difference.seconds < 60): 
                return Response({"message":"Action not allowed, please wait one minute after your last command...", "data": []}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Commonde.DoesNotExist:
            pass
        
        prodCarts = ProductCart.objects.filter(cart = shoppingCart)
        finalPrice = 0
        for prodCart in prodCarts:
            finalPrice = finalPrice + prodCart.finalPrix
        serialize = ShoppingCartSerializer(shoppingCart)       

        shoppingCart.validated = True
        command = Commonde(user = user, cart = shoppingCart)
        command.save()
        shoppingCart.save()
        return Response({"message" :"Order placed successfully...", "data": serialize.data, "prix_finale" : finalPrice}, status = status.HTTP_202_ACCEPTED)


# @api_view(['GET'])
# def shopping_cart(request):
#     if request.method == 'GET':
#         try:
#             user = User.objects.get(prenom = "Adnane")
#         except User.DoesNotExist:
#             return Response("User not found")
#         shopCart = ShoppingCart.objects.get(user = user, validated = False)
#         prodCarts = ProductCart.objects.filter(cart = shopCart)
#         finalPrice = 0
#         for prodCart in prodCarts:
#             finalPrice = finalPrice + prodCart.finalPrix
#         serialize = ShoppingCartSerializer(shopCart)
#         return Response({"data": serialize.data, "prix_finale" : finalPrice}, status=status.HTTP_200_OK)
        