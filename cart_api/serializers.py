from rest_framework import serializers
from simplejson import OrderedDict
from cart_api.models import ShoppingCart, User, ProductCart
from product_api.serializers import ProductSerializer



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('code','nom','prenom')
    
    def to_representation(self, instance):
        datas = super().to_representation(instance)
        return OrderedDict([(key, datas[key]) for key in datas if datas[key] is not None])


class ProductCartSerializer(serializers.ModelSerializer):

    remise = serializers.FloatField(source="remisePrix", allow_null=True)
    prix_finale = serializers.FloatField(source="finalPrix")
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductCart
        fields = ('quantity','prix','remise','prix_finale','product')

    def to_representation(self, instance):
        datas = super().to_representation(instance)
        return  OrderedDict([(key, datas[key]) for key in datas if datas[key] is not None])


class ShoppingCartSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    product_carts = ProductCartSerializer(many=True, read_only=True)

    class Meta:
        model = ShoppingCart
        fields = ('user','validated', 'product_carts')

