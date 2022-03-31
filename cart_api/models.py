from django.db import models

from product_api.models import Product

# Create your models here.

class User(models.Model):
    code = models.CharField(max_length=100)
    nom = models.CharField(max_length=20, blank=True, null=True)
    prenom = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=100, blank=True, null=True)


class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    validated = models.BooleanField(default=False) # pour savoir si l'utilisateur est entrain d'acheter des produits , ou a déjà passer la commande


class Commonde(models.Model): # sauvegarder les achats effectués par nos clients comme historiques, et ça servira aussi de moyen pour savoir si l'utulisateur à déjà effectué une commande dans moins d'une minute

   
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_command")
    date = models.DateField(auto_now_add=True)
    cart = models.OneToOneField(ShoppingCart, on_delete=models.SET_NULL, related_name="cart", blank=True, null=True)


class ProductCart(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField()
    prix = models.FloatField()
    remisePrix = models.FloatField()
    finalPrix = models.FloatField()

    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name="cart_shopping")



