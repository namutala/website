# Generated by Django 5.0.4 on 2024-04-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0014_rename_description_item_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='short_description',
            field=models.TextField(default='description', max_length=150),
        ),
    ]
