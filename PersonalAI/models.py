# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, null=True)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    nationality = models.CharField(max_length=100, null=True)
    languages_spoken = models.TextField(null=True)  # Comma-separated languages
    education = models.CharField(max_length=255, null=True)
    work_history = models.TextField(null=True)
    hobbies = models.TextField(null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

# Family and Relationships
class FamilyMember(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="family_members")
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=50)
    birthday = models.DateField()
    notes = models.TextField()

# Daily Schedule and Tasks
class DailyTask(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="tasks")
    date = models.DateField()
    time = models.TimeField()
    event = models.CharField(max_length=255)
    notes = models.TextField()

# Communication Contacts
class Contact(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="contacts")
    name = models.CharField(max_length=255)
    relation = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

# Financial Information
class FinancialInfo(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="financial_info")
    item = models.CharField(max_length=255)
    monthly_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField()

# Health and Fitness
class HealthFitness(models.Model):
    Profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="health_fitness")
    health_goals = models.TextField()
    allergies = models.CharField(max_length=255)
    medications = models.TextField()

# Travel
class Travel(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="travels")
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.TextField()

# Favorite Items
class FavoriteItem(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="favorites")
    item_type = models.CharField(max_length=255)
    favorite_item = models.CharField(max_length=255)

# Digital Data
class DigitalDevice(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="digital_devices")
    device = models.CharField(max_length=255)
    device_type = models.CharField(max_length=100)
    notes = models.TextField()

# Professional Information
class ProfessionalInfo(models.Model):
    Profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="professional_info")
    current_role = models.CharField(max_length=255)
    certifications = models.TextField()

# Recent Updates
class RecentUpdate(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="recent_updates")
    date = models.DateField()
    update = models.TextField()

# Contextual and Historical Information
class HistoricalEvent(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="historical_events")
    event = models.CharField(max_length=255)
    date = models.DateField()
    notes = models.TextField()

# Security and Preferences
class SecurityPreference(models.Model):
    Profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="security_preferences")
    emergency_contact = models.CharField(max_length=255)
    privacy_settings = models.TextField()

# Smart Home Integration
class SmartHomeDevice(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="smart_home_devices")
    device = models.CharField(max_length=255)
    device_type = models.CharField(max_length=100)
    notes = models.TextField()

# Assets
class Asset(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="assets")
    asset_type = models.CharField(max_length=100)
    description = models.TextField()
    date_purchased = models.DateField()
    purchase_price = models.DecimalField(max_digits=15, decimal_places=2)
    down_payment = models.DecimalField(max_digits=10, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    date_sold = models.DateField(null=True, blank=True)
    sale_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    notes = models.TextField()

# Insurance
class Insurance(models.Model):
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="insurances")
    insurance_type = models.CharField(max_length=100)
    provider = models.CharField(max_length=255)
    policy_number = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    coverage_details = models.TextField()
    linked_asset = models.CharField(max_length=255, null=True, blank=True)
    notes = models.TextField()
