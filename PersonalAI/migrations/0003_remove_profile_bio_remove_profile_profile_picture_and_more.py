# Generated by Django 5.1.4 on 2024-12-13 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PersonalAI', '0002_financialdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='status',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='education',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hobbies',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='languages_spoken',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nationality',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='work_history',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_type', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_purchased', models.DateField()),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('down_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_sold', models.DateField(blank=True, null=True)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('notes', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('relation', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='DailyTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('event', models.CharField(max_length=255)),
                ('notes', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='DigitalDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=255)),
                ('device_type', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='digital_devices', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('notes', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='family_members', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=255)),
                ('favorite_item', models.CharField(max_length=255)),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='FinancialInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=255)),
                ('monthly_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notes', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='financial_info', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='HealthFitness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('health_goals', models.TextField()),
                ('allergies', models.CharField(max_length=255)),
                ('medications', models.TextField()),
                ('Profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='health_fitness', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('notes', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historical_events', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance_type', models.CharField(max_length=100)),
                ('provider', models.CharField(max_length=255)),
                ('policy_number', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coverage_details', models.TextField()),
                ('linked_asset', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insurances', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_role', models.CharField(max_length=255)),
                ('certifications', models.TextField()),
                ('Profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='professional_info', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='RecentUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('update', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recent_updates', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='SecurityPreference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emergency_contact', models.CharField(max_length=255)),
                ('privacy_settings', models.TextField()),
                ('Profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='security_preferences', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='SmartHomeDevice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=255)),
                ('device_type', models.CharField(max_length=100)),
                ('notes', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='smart_home_devices', to='PersonalAI.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('notes', models.TextField()),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels', to='PersonalAI.profile')),
            ],
        ),
        migrations.DeleteModel(
            name='FinancialData',
        ),
    ]
