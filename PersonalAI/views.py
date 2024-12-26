from django.shortcuts import render
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import status, viewsets
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

    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = PersonalProfile.objects.all()
    serializer_class = ProfileSerializer

class EducationViewSet(generics.CreateAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

    
    def get(self, request, *args, **kwargs):
        # Get a specific Education record or list all records
        if 'pk' in kwargs:
            # If 'pk' is in the URL, return a single Education object
            education = self.get_object()
            serializer = self.get_serializer(education)
            return Response(serializer.data)
        else:
            # If no 'pk', return a list of all Education records
            education = self.get_queryset()
            serializer = self.get_serializer(education, many=True)
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        # Full update (replace the Education record)
        education = self.get_object()  # Get the specific record to update
        serializer = self.get_serializer(education, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        # Partial update (modify specific fields of the Education record)
        education = self.get_object()  # Get the specific record to update
        serializer = self.get_serializer(education, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, request, *args, **kwargs):
    #     # You can add custom logic here before or after updating the profile
    #     # For example, logging or additional validation
    #     response = super().update(request, *args, **kwargs)
    #     return response

class WorkViewSet(generics.CreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

    
    def get(self, request, *args, **kwargs):
        # Get a specific Education record or list all records
        if 'pk' in kwargs:
            # If 'pk' is in the URL, return a single Education object
            work = self.get_object()
            serializer = self.get_serializer(work)
            return Response(serializer.data)
        else:
            # If no 'pk', return a list of all Education records
            work = self.get_queryset()
            serializer = self.get_serializer(work, many=True)
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        # Full update (replace the Education record)
        work = self.get_object()  # Get the specific record to update
        serializer = self.get_serializer(work, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        # Partial update (modify specific fields of the Education record)
        work = self.get_object()  # Get the specific record to update
        serializer = self.get_serializer(work, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class FamilyRelationshipViewSet (generics.CreateAPIView):
    queryset = FamilyRelationship.objects.all()
    serializer_class = FamilyRelationshipSerializer

    
    def get(self, request, *args, **kwargs):
        # Get a specific Education record or list all records
        if 'pk' in kwargs:
            # If 'pk' is in the URL, return a single Education object
            family = self.get_object()
            serializer = self.get_serializer(family)
            return Response(serializer.data)
        else:
            # If no 'pk', return a list of all Education records
            family = self.get_queryset()
            serializer = self.get_serializer(family, many=True)
            return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        # Full update (replace the Education record)
        family = self.get_object()  # Get the specific record to update
        serializer = self.get_serializer(family, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        # Partial update (modify specific fields of the Education record)
        family = self.get_object()  # Get the specific record to update
        serializer = self.get_serializer(family, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
