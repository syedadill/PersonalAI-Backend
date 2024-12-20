# models.py
from django.db import models
from django.contrib.auth.models import User

# Personal Profile
class PersonalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    nationality = models.CharField(max_length=50)
    languages_spoken = models.TextField()


    def __str__(self):
        return f"{self.user.username}'s Profile"



# Education
class Education(models.Model):
#profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='education', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True )
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    institution_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    achievements = models.TextField(null=True, blank=True)

# Work Experience
class Work(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='work')
    from_date = models.DateField()
    to_date = models.DateField(null=True, blank=True)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    supervisor_name = models.CharField(max_length=50, null=True, blank=True)
    supervisor_phone = models.CharField(max_length=20, null=True, blank=True)
    supervisor_email = models.EmailField(null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True)
    achievements = models.TextField(null=True, blank=True)

# Family and Relationships
class FamilyRelationship(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='family')
    name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=50)
    birthday = models.DateField()
    notes = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

# Cars
class Car(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='cars')
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    vin = models.CharField(max_length=50)
    licence_plate = models.CharField(max_length=20)
    date_purchased = models.DateField()
    odometer_at_purchase = models.IntegerField()
    total_purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()
    down_payment = models.DecimalField(max_digits=10, decimal_places=2)
    financed_amount = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_payment = models.DecimalField(max_digits=10, decimal_places=2)

# Real Estate
class RealEstate(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='real_estate')
    type = models.CharField(max_length=50)
    sq_ft = models.IntegerField()
    lot_size = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    year_built = models.IntegerField(null=True, blank=True)

# Mortgage
class Mortgage(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, related_name='mortgage')
    financial_institution = models.CharField(max_length=100)
    monthly_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    period = models.CharField(max_length=10)  # e.g., 30Y
    property_cost = models.DecimalField(max_digits=10, decimal_places=2)
    down_percent = models.FloatField()
    down_payment = models.DecimalField(max_digits=10, decimal_places=2)
    loan_amount = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.FloatField()
    apr = models.FloatField()
    upfront_cost = models.DecimalField(max_digits=10, decimal_places=2)

class HealthFitness(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='health_fitness', null=True)
    blood_type = models.CharField(max_length=5, null=True, blank=True)
    allergies = models.TextField(null=True, blank=True)
    medications = models.TextField(null=True, blank=True)


# Travel History
class TravelHistory(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='travel_history')
    destination = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    notes = models.TextField(null=True, blank=True)

# Travel Memberships
class TravelMembership(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='travel_memberships')
    type = models.CharField(max_length=50)  # e.g., Hotel, Car Rental
    company = models.CharField(max_length=100)
    membership_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    notes = models.TextField(null=True, blank=True)

# Celebrations
class Celebration(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='celebrations')
    event = models.CharField(max_length=100)
    person = models.CharField(max_length=100)
    date = models.DateField()
    first_event_date = models.DateField()
    notes = models.TextField(null=True, blank=True)

# Insurance
class Insurance(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='insurance', null = True)
    type = models.CharField(max_length=50, null=True)  # e.g., Car, Home
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_details = models.TextField()
    linked_asset = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True)



# Personal Preferences
class PersonalPreference(models.Model):
    profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE, related_name='personal_preferences')
    type = models.CharField(max_length=50)  # e.g., Cuisine, Movie Genre
    favorite_item = models.CharField(max_length=100)