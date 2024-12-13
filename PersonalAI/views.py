from django.shortcuts import render
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from .models import *

class RegisterView(generics.CreateAPIView):
    queryset= User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# class ProfileDetailView(generics.RetrieveUpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [IsAuthenticated]

#     def get_object(self):
#         return self.request.user.profile

    

from rest_framework.views import APIView

class OnboardingAPIView(APIView):
    """
    Handles onboarding data creation and retrieval.
    """
    def get(self, request):
        # Retrieve all onboarding entries
        onboarding_data = Profile.objects.all()
        serializer = ProfileSerializer(onboarding_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Create a new onboarding entry
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

