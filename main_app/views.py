from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer


class UserRegisterView(APIView):
    def post(self, request):
        # Initiate the serializer with the request data
        serializer = UserRegistrationSerializer(data=request.data)

        # Data validation
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        
        # If data is invalid, return the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)