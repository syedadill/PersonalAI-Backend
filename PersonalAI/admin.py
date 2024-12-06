from django.contrib import admin

# Register your models here.
from .models import *  # Import the custom Profile model

# Register the Profile model in the admin interface
admin.site.register(Profile)