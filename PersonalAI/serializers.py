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
        
        # Create a Profile instance for the new user
        Profile.objects.create(user=user)

        return user
    
    





class FamilyMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyMember
        fields = '__all__'
        

class DailyTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTask
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class FinancialInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialInfo
        fields = '__all__'

class HealthFitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFitness
        fields = '__all__'

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'

class DigitalDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalDevice
        fields = '__all__'

class ProfessionalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionalInfo
        fields = '__all__'

class RecentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentUpdate
        fields = '__all__'

class HistoricalEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalEvent
        fields = '__all__'

class SecurityPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityPreference
        fields = '__all__'

class SmartHomeDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartHomeDevice
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = '__all__'


#class ProfSerializer(serializers.ModelSerializer):
   # class Meta:
      #  model = Profile
       # field = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    #profile = ProfSerializer(many=True, required= False)
    family_members = FamilyMemberSerializer(many=True, required=False)
    tasks = DailyTaskSerializer(many=True, required=False)
    contacts = ContactSerializer(many=True, required=False)
    financial_info = FinancialInfoSerializer(many=True, required=False)
    health_fitness = HealthFitnessSerializer(required=False)
    travels = TravelSerializer(many=True, required=False)
    favorites = FavoriteItemSerializer(many=True, required=False)
    digital_devices = DigitalDeviceSerializer(many=True, required=False)
    professional_info = ProfessionalInfoSerializer(required=False)
    recent_updates = RecentUpdateSerializer(many=True, required=False)
    historical_events = HistoricalEventSerializer(many=True, required=False)
    security_preferences = SecurityPreferenceSerializer(required=False)
    smart_home_devices = SmartHomeDeviceSerializer(many=True, required=False)
    assets = AssetSerializer(many=True, required=False)
    insurances = InsuranceSerializer(many=True, required=False)

    class Meta:
        model = Profile
        fields = '__all__'


    def create(self, validated_data):
        # Extract nested data
        nested_data = {
            "family_members": validated_data.pop('family_members', []),
            "tasks": validated_data.pop('tasks', []),
            "contacts": validated_data.pop('contacts', []),
            "financial_info": validated_data.pop('financial_info', []),
            "travels": validated_data.pop('travels', []),
            "favorites": validated_data.pop('favorites', []),
            "digital_devices": validated_data.pop('digital_devices', []),
            "recent_updates": validated_data.pop('recent_updates', []),
            "historical_events": validated_data.pop('historical_events', []),
            "smart_home_devices": validated_data.pop('smart_home_devices', []),
            "assets": validated_data.pop('assets', []),
            "insurances": validated_data.pop('insurances', []),
        }

        # Create main onboarding instance
        onboarding = Profile.objects.create(**validated_data)

        # Create related instances
        for key, items in nested_data.items():
            model = getattr(onboarding, key)
            for item in items:
                model.create(**item)

        # Create one-to-one relations
        if 'health_fitness' in validated_data:
            HealthFitness.objects.create(onboarding=onboarding, **validated_data['health_fitness'])
        if 'professional_info' in validated_data:
            ProfessionalInfo.objects.create(onboarding=onboarding, **validated_data['professional_info'])
        if 'security_preferences' in validated_data:
            SecurityPreference.objects.create(onboarding=onboarding, **validated_data['security_preferences'])

        return onboarding
