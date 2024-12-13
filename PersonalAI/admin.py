from django.contrib import admin

# Register your models here.
from .models import *  # Import the custom Profile model

# Register the Profile model in the admin interface
admin.site.register(Profile)
admin.site.register(FamilyMember)
admin.site.register(DailyTask)
admin.site.register(Contact)
admin.site.register(FinancialInfo)
admin.site.register(HealthFitness)
admin.site.register(Travel)
admin.site.register(FavoriteItem)
admin.site.register(DigitalDevice)
admin.site.register(ProfessionalInfo)
admin.site.register(RecentUpdate)
admin.site.register(HistoricalEvent)
admin.site.register(SecurityPreference)
admin.site.register(SmartHomeDevice)
admin.site.register(Asset)
admin.site.register(Insurance)
