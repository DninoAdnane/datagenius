from django.db import models
from product_api.enumModels import Rayon, TypeRemise

# Create your models here.

class Remise(models.Model):
    typeRemise = models.CharField(max_length=10, choices=TypeRemise.choices, default=TypeRemise.OFFRE)
    nbAchete = models.IntegerField(blank=True, null=True)
    nbOffer = models.IntegerField(blank=True, null= True)
    tauxRed = models.IntegerField(blank=True, null=True)



class Product(models.Model):
    name = models.CharField(max_length=30)
    prix = models.FloatField
    rayon = models.CharField(max_length=20, choices=Rayon.choices, default=Rayon.ALIMENTAIRE)
    remise = models.ForeignKey(Remise, related_name="remises", on_delete=models.CASCADE, blank=True, null=True)