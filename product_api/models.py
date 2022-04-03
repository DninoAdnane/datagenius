from django.db import models
from product_api.enumModels import Rayon, TypeRemise

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    prix = models.FloatField()
    rayon = models.CharField(max_length=20, choices=Rayon.choices, default=Rayon.ALIMENTAIRE)
    quantite = models.IntegerField()

class Remise(models.Model):
    typeRemise = models.CharField(max_length=10, choices=TypeRemise.choices, default=TypeRemise.OFFRE)
    nbAchete = models.IntegerField(blank=True, null=True)
    nbOffer = models.IntegerField(blank=True, null= True)
    tauxRed = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name="remises" ) # Je suppose ici qu'un produit pour avoir plus remises



