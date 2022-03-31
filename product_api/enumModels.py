from django.db import models

#Le fichier suivant contient les choix d'énumération qu'on peut avoir pour le model Product et Remise

class TypeRemise(models.TextChoices): #Remise disponibles
        OFFRE = 'Offre'
        REDUCTION = 'Reduction'


class Rayon(models.TextChoices): # Exemple de rayon disponibles
        ALIMENTAIRE = 'Alimentaire'
        TEXTILE = 'Textile'
        INFORMATIQUE = 'Informatique'
        FRAIS= 'Frais'
        BOUCHERIE = 'Boucherie'