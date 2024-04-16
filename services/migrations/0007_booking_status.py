# Generated by Django 5.0 on 2024-04-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_service_contact_service_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Booked', 'Booked'), ('Cancelled', 'Cancelled')], default='Pending', max_length=18),
        ),
    ]