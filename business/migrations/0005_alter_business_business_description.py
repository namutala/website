# Generated by Django 5.0.3 on 2024-03-20 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0004_rename_user_business_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='business_description',
            field=models.TextField(max_length=50),
        ),
    ]
