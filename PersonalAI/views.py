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


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    
