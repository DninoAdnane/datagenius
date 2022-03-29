from django.db import models

class TypeRemise(models.TextChoices):
        OFFRE = 'Offre'
        REDUCTION = 'Reduction'


class Rayon(models.TextChoices): # Exemple de rayon disponibles
        ALIMENTAIRE = 'Alimentaire'
        TEXTILE = 'Textile'
        INFORMATIQUE = 'Informatique'
        FRAIS= 'Frais'
        BOUCHERIE = 'Boucherie'