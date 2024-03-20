# Generated by Django 5.0.3 on 2024-03-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0006_alter_business_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='business',
            name='business_name',
            field=models.CharField(default='Business name', max_length=35),
        ),
        migrations.AlterField(
            model_name='business',
            name='location',
            field=models.TextField(max_length=50),
        ),
    ]