# Generated by Django 4.1.3 on 2022-11-17 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Variation',
            new_name='Color',
        ),
    ]
