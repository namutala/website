# Generated by Django 5.0.4 on 2024-04-10 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storefront', '0019_alter_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
    ]
