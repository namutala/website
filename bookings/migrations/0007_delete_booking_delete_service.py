# Generated by Django 5.0 on 2024-03-26 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0006_remove_booking_date_booked'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='service',
        ),
    ]
