from rest_framework import serializers
from .models import User

# class UserSerializer()


class LoginSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(max_length = 120, min_length = 6, write_only = True)

    class Meta:
        model = User
        fields = ('token')