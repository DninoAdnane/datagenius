from rest_framework import serializers
from simplejson import OrderedDict
from product_api.enumModels import Rayon, TypeRemise
from product_api.models import Product, Remise


class RemiseSerializer(serializers.ModelSerializer):
    remise = serializers.CharField(source = "typeRemise", allow_null = True)
    acheter = serializers.IntegerField(source = "nbAchete", allow_null = True)
    offerts = serializers.IntegerField(source = "nbOffer", allow_null = True)
    reduction = serializers.IntegerField(source = "tauxRed", allow_null = True)

    class Meta:
        model = Remise
        fields = ('remise','acheter','offerts','reduction')
    
    def to_representation(self, instance):
        datas = super().to_representation(instance)
        return  OrderedDict([(key, datas[key]) for key in datas if datas[key] is not None])


class ProductSerializer(serializers.ModelSerializer):
    
    remises = RemiseSerializer(many=True, read_only = True)
    
    class Meta:
        model = Product
        fields = ('name', 'prix' , 'rayon', 'remises')

    def to_representation(self, instance):
        datas = super().to_representation(instance)
        return datas

