# Generated by Django 5.0.3 on 2024-03-27 02:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_rename_srvice_description_service_service_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='serviceImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service_images')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='services.service')),
            ],
        ),
    ]
