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
        #PersonalProfile.objects.create(user=user)

        return user
    
    





class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'
        

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class FamilyRelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamilyRelationship
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class RealEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'

class MortgageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortgage
        fields = '__all__'

class HealthFitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthFitness
        fields = '__all__'

class TravelHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelHistory
        fields = '__all__'

class TravelMembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelMembership
        fields = '__all__'

class PersonalPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalPreference
        fields = '__all__'

class CelebrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Celebration
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
    education = EducationSerializer(many=True, required=False)
    work = WorkSerializer(many=True, required=False)
    family_relationship = FamilyRelationshipSerializer(many=True, required=False)
    car = CarSerializer(many=True, required=False)
    real_estate = RealEstateSerializer(many=True, required=False)
    mortgage = MortgageSerializer(many=True, required=False)
    health_fitness = HealthFitnessSerializer(many=True, required=False)
    travel_history = TravelHistorySerializer(many=True, required=False)
    travel_membership = TravelMembershipSerializer(many=True, required=False)
    personal_preference = PersonalPreferenceSerializer(many=True, required=False)
    celebration = CelebrationSerializer(many=True, required=False)
    insurance = InsuranceSerializer(many=True, required=False)

    class Meta:
        model = PersonalProfile
        fields = '__all__'

    def create(self, validated_data):
        # Extract nested data
        education_data = validated_data.pop('education', [])
        work_data = validated_data.pop('work', [])
        family_relationship_data = validated_data.pop('family_relationship', [])
        car_data = validated_data.pop('car', [])
        real_estate_data = validated_data.pop('real_estate', [])
        mortgage_data = validated_data.pop('mortgage', [])
        health_fitness_data = validated_data.pop('health_fitness', [])
        travel_history_data = validated_data.pop('travel_history', [])
        travel_membership_data = validated_data.pop('travel_membership', [])
        personal_preference_data = validated_data.pop('personal_preference', [])
        celebration_data = validated_data.pop('celebration', [])
        insurance_data = validated_data.pop('insurance', [])

        # Create the main profile
        profile = PersonalProfile.objects.create(**validated_data)

        # Create related objects
        self._create_related_objects(profile, education_data, work_data, family_relationship_data, 
                                     car_data, real_estate_data, mortgage_data, health_fitness_data, 
                                     travel_history_data, travel_membership_data, personal_preference_data, 
                                     celebration_data, insurance_data)
        
        return profile

    def update(self, instance, validated_data):
        # Extract nested data
        education_data = validated_data.pop('education', None)
        work_data = validated_data.pop('work', None)
        family_relationship_data = validated_data.pop('family_relationship', None)
        car_data = validated_data.pop('car', None)
        real_estate_data = validated_data.pop('real_estate', None)
        mortgage_data = validated_data.pop('mortgage', None)
        health_fitness_data = validated_data.pop('health_fitness', None)
        travel_history_data = validated_data.pop('travel_history', None)
        travel_membership_data = validated_data.pop('travel_membership', None)
        personal_preference_data = validated_data.pop('personal_preference', None)
        celebration_data = validated_data.pop('celebration', None)
        insurance_data = validated_data.pop('insurance', None)

        # Update the main profile instance
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Update related objects if data is provided
        self._update_related_objects(instance, education_data, work_data, family_relationship_data, 
                                      car_data, real_estate_data, mortgage_data, health_fitness_data, 
                                      travel_history_data, travel_membership_data, personal_preference_data, 
                                      celebration_data, insurance_data)
        
        return instance

    def _create_related_objects(self, profile, education_data, work_data, family_relationship_data, 
                                 car_data, real_estate_data, mortgage_data, health_fitness_data, 
                                 travel_history_data, travel_membership_data, personal_preference_data, 
                                 celebration_data, insurance_data):
        for education in education_data:
            Education.objects.create(profile=profile, **education)
        for work in work_data:
            Work.objects.create(profile=profile, **work)
        for family_relationship in family_relationship_data:
            FamilyRelationship.objects.create(profile=profile, **family_relationship)
        for car in car_data:
            Car.objects.create(profile=profile, **car)
        for real_estate in real_estate_data:
            RealEstate.objects.create(profile=profile, **real_estate)
        for mortgage in mortgage_data:
            Mortgage.objects.create(profile=profile, **mortgage)
        for health_fitness in health_fitness_data:
            HealthFitness.objects.create(profile=profile, **health_fitness)
        for travel_history in travel_history_data:
            TravelHistory.objects.create(profile=profile, **travel_history)
        for travel_membership in travel_membership_data:
            TravelMembership.objects.create(profile=profile, **travel_membership)
        for personal_preference in personal_preference_data:
            PersonalPreference.objects.create(profile=profile, **personal_preference)
        for celebration in celebration_data:
            Celebration.objects.create(profile=profile, **celebration)
        for insurance in insurance_data:
            Insurance.objects.create(profile=profile, **insurance)

    def _update_related_objects(self, instance, education_data, work_data, family_relationship_data, 
                                car_data, real_estate_data, mortgage_data, health_fitness_data, 
                                travel_history_data, travel_membership_data, personal_preference_data, 
                                celebration_data, insurance_data):
        if education_data is not None:
            instance.education.all().delete()
            for education in education_data:
                Education.objects.create(profile=instance, **education)
        if work_data is not None:
            instance.work.all().delete()
            for work in work_data:
                Work.objects.create(profile=instance, **work)
        if family_relationship_data is not None:
            instance.family_relationship.all().delete()
            for family_relationship in family_relationship_data:
                FamilyRelationship.objects.create(profile=instance, **family_relationship)
        if car_data is not None:
            instance.car.all().delete()
            for car in car_data:
                Car.objects.create(profile=instance, **car)
        if real_estate_data is not None:
            instance.real_estate.all().delete()
            for real_estate in real_estate_data:
                RealEstate.objects.create(profile=instance, **real_estate)
        if mortgage_data is not None:
            instance.mortgage.all().delete()
            for mortgage in mortgage_data:
                Mortgage.objects.create(profile=instance, **mortgage)
        if health_fitness_data is not None:
            instance.health_fitness.all().delete()
            for health_fitness in health_fitness_data:
                HealthFitness.objects.create(profile=instance, **health_fitness)
        if travel_history_data is not None:
            instance.travel_history.all().delete()
            for travel_history in travel_history_data:
                TravelHistory.objects.create(profile=instance, **travel_history)
        if travel_membership_data is not None:
            instance.travel_membership.all().delete()
            for travel_membership in travel_membership_data:
                TravelMembership.objects.create(profile=instance, **travel_membership)
        if personal_preference_data is not None:
            instance.personal_preference.all().delete()
            for personal_preference in personal_preference_data:
                PersonalPreference.objects.create(profile=instance, **personal_preference)
        if celebration_data is not None:
            instance.celebration.all().delete()
            for celebration in celebration_data:
                Celebration.objects.create(profile=instance, **celebration)
        if insurance_data is not None:
            instance.insurance.all().delete()
            for insurance in insurance_data:
                Insurance.objects.create(profile=instance, **insurance)
