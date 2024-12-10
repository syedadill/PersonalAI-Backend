# models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    status = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


class FinancialData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_assets = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2)
    monthly_expenses = models.DecimalField(max_digits=10, decimal_places=2)