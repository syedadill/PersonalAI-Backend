# Generated by Django 5.1.4 on 2024-12-19 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalAI', '0008_alter_personalprofile_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='personalprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='personalprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='personalprofile',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='personalprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='personalprofile',
            name='zip_code',
        ),
    ]
