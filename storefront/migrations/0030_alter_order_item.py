# Generated by Django 5.0.4 on 2024-04-10 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0029_alter_order_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='storefront.item'),
        ),
    ]
