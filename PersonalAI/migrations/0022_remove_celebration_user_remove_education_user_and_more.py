# Generated by Django 5.1.4 on 2024-12-27 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalAI', '0021_alter_car_user_alter_celebration_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celebration',
            name='user',
        ),
        migrations.RemoveField(
            model_name='education',
            name='user',
        ),
        migrations.RemoveField(
            model_name='familyrelationship',
            name='user',
        ),
        migrations.RemoveField(
            model_name='healthfitness',
            name='user',
        ),
        migrations.RemoveField(
            model_name='insurance',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mortgage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='personalpreference',
            name='user',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='user',
        ),
        migrations.RemoveField(
            model_name='travelhistory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='travelmembership',
            name='user',
        ),
        migrations.RemoveField(
            model_name='work',
            name='user',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='Celebration',
        ),
        migrations.DeleteModel(
            name='Education',
        ),
        migrations.DeleteModel(
            name='FamilyRelationship',
        ),
        migrations.DeleteModel(
            name='HealthFitness',
        ),
        migrations.DeleteModel(
            name='Insurance',
        ),
        migrations.DeleteModel(
            name='Mortgage',
        ),
        migrations.DeleteModel(
            name='PersonalPreference',
        ),
        migrations.DeleteModel(
            name='RealEstate',
        ),
        migrations.DeleteModel(
            name='TravelHistory',
        ),
        migrations.DeleteModel(
            name='TravelMembership',
        ),
        migrations.DeleteModel(
            name='Work',
        ),
    ]
