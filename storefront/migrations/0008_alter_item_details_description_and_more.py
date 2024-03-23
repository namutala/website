# Generated by Django 5.0.3 on 2024-03-23 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0007_item_details_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_details',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='item_details',
            name='key_features',
            field=models.TextField(max_length=200),
        ),
    ]
