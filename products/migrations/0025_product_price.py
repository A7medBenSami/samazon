# Generated by Django 4.1.3 on 2022-11-25 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_rename_img_product_default_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
    ]
