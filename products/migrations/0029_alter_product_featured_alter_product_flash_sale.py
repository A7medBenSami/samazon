# Generated by Django 4.1.3 on 2022-11-28 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_product_flash_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Featured',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='flash_sale',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
