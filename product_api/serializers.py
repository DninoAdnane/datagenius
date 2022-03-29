from rest_framework import serializers
from enumModels import Rayon, TypeRemise
from models import Product


class RemiseSerializer(serializers.ModelSerializer):
    typeRemise = serializers.CharField(max_length=10, choices=TypeRemise.choices, default=TypeRemise.OFFRE)
    nbAchete = serializers.IntegerField(blank=True, null=True)
    nbOffer = serializers.IntegerField(blank=True, null= True)
    tauxRed = serializers.IntegerField(blank=True, null=True)


class ProductSerializer(serializers.ModelSerializer):
    remise = serializers.CharField(source = "remise.typeRemise")
    acheter = serializers.IntegerField(source = "remise.nbAcheter")
    offerts = serializers.IntegerField(source = "remise.nbOffer")
    reduction = serializers.IntegerField(source = "remise.tauxRed")
    
    class Meta:
        model = Product
        fields = "__al__"