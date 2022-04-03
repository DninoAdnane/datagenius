from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from datetime import datetime, timezone
from django.contrib.auth.hashers import make_password

from product_api.models import Product
from auth_api.models import User

# Create your models here.    



class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    validated = models.BooleanField(default=False) # pour savoir si l'utilisateur est entrain d'acheter des produits , ou a déjà passer la commande


class Commonde(models.Model): # sauvegarder les achats effectués par nos clients comme historiques, et ça servira aussi de moyen pour savoir si l'utulisateur à déjà effectué une commande dans moins d'une minute

   
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_command")
    date = models.DateTimeField(auto_now_add=True)
    cart = models.OneToOneField(ShoppingCart, on_delete=models.SET_NULL, related_name="cart", blank=True, null=True)


class ProductCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product")
    quantity = models.IntegerField()
    prix = models.FloatField()
    remisePrix = models.FloatField()
    finalPrix = models.FloatField()

    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name="product_carts")




