# Generated by Django 5.0.3 on 2024-03-20 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0008_image_catalogoue_delete_businessimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catalogoue',
            new_name='Catalogue',
        ),
    ]
