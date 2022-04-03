from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from auth_api.serializers import LoginSerializer, SignInSerializer

# Create your views here.



@api_view(['POST'])
def signin(request):
    serializer = SignInSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message":"Your account had been created successfully...", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"message":"Something went wrong...", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    code = request.data.get('code')
    email = request.data.get('email')
    password = request.data.get('password')
    if code is None or password is None:
        return Response({"message":"request fields error...", "data": []}, status=status.HTTP_400_BAD_REQUEST)
        
    user = authenticate(code = code, email = email, password = password)
    print(code)

    if user:
        serializer = LoginSerializer(user)
        return Response({"message" :"User logged successfully", "data": serializer.data}, status = status.HTTP_202_ACCEPTED)
    else:
        return Response({"message" :"Please try again and check your credentials....", "data": []}, status = status.HTTP_401_UNAUTHORIZED)
        