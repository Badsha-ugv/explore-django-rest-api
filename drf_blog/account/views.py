from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from .serializers import UserSerializer


@api_view(["POST"])
def user_registration(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            print("User ", user)
            token = Token.objects.get(user=user)
            print("Token ", token)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors)
