from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import *


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match"})
        return attrs    

    def create(self, validated_data):
        # Remove password2 as it's not part of the User model
        validated_data.pop('password2')
        
        # Create the user instance
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        
        # # Create a Profile instance for the new user
        # Profile.objects.create(user=user)

        # return user

# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = '__all__'
      

# class EducationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Education
#         fields = '__all__'
        

# class WorkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Work
#         fields = '__all__'

# class FamilyRelationshipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = FamilyRelationship
#         fields = '__all__'

# class CarSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Car
#         fields = '__all__'

# class RealEstateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RealEstate
#         fields = '__all__'

# class MortgageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Mortgage
#         fields = '__all__'

# class HealthFitnessSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = HealthFitness
#         fields = '__all__'

# class TravelHistorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TravelHistory
#         fields = '__all__'

# class TravelMembershipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TravelMembership
#         fields = '__all__'

# class PersonalPreferenceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = PersonalPreference
#         fields = '__all__'

# class CelebrationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Celebration
#         fields = '__all__'


# class InsuranceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Insurance
#         fields = '__all__'


class ChatRequestSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000)

class UploadFileSerializer(serializers.Serializer):
    file = serializers.FileField()