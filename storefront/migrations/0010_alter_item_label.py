# Generated by Django 5.0.3 on 2024-03-24 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0009_alter_item_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('new', 'new'), ('flash sale', 'flash sale'), ('limited', 'limited')], default=None, max_length=15),
        ),
    ]