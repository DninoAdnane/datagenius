from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from auth_api.serializers import LoginSerializer

# Create your views here.

@api_view(['POST'])
def login(request):
    code = request.data.get('code')
    password = request.data.get('password')
    if code is None or password is None:
        return Response({"message":"request fields error...", "data": []}, status=status.HTTP_400_BAD_REQUEST)
        
    user = authenticate(username = code, password = password)

    if user:
        serializer = LoginSerializer(user)
        return Response({"message" :"User logged successfully", "data": serializer.data}, status = status.HTTP_202_ACCEPTED)
    else:
        return Response({"message" :"Please try again and check your credentials....", "data": []}, status = status.HTTP_401_UNAUTHORIZED)
        