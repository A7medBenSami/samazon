# Generated by Django 4.1.3 on 2022-11-17 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_rename_color_color_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='color',
            old_name='name',
            new_name='color',
        ),
    ]