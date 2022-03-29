from django.db import models

# Create your models here.


class TypeRemise(models.TextChoices):
        OFFRE = 'Offre'
        REDUCTION = 'Reduction'

class Remise(models.Model):
    typeRemise = models.CharField(max_length=10, choices=TypeRemise.choices, default=TypeRemise.OFFRE)
    nbAchete = models.IntegerField(blank=True, null=True)
    nbOffer = models.IntegerField(blank=True, null= True)
    tauxRed = models.IntegerField(blank=True, null=True)



class Product(models.Model):

    class Rayon(models.TextChoices): # Exemple de rayon disponibles
        ALIMENTAIRE = 'Alimentaire'
        TEXTILe = 'Textile'
        INFORMATIQUE = 'Informatique'
        TEXTILE= 'Textile'
        BOUCHERIE = 'Boucherie'

    name = models.CharField(max_length=30)
    prix = models.FloatField
    rayon = models.CharField(max_length=20, choices=Rayon.choices, default=Rayon.ALIMENTAIRE)
    remise = models.ForeignKey(Remise, on_delete=models.CASCADE)