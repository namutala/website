# Generated by Django 5.0.3 on 2024-03-27 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_serviceimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_name',
            field=models.CharField(max_length=100),
        ),
    ]