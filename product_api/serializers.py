from rest_framework import serializers
from simplejson import OrderedDict
from enumModels import Rayon, TypeRemise
from models import Product


class ProductSerializer(serializers.ModelSerializer):
    remise = serializers.CharField(source = "remise.typeRemise")
    acheter = serializers.IntegerField(source = "remise.nbAcheter")
    offerts = serializers.IntegerField(source = "remise.nbOffer")
    reduction = serializers.IntegerField(source = "remise.tauxRed")
    
    class Meta:
        model = Product
        fields = "__al__"

    def to_representation(self, instance):
        result = super(ProductSerializer, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None])