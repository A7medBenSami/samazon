# Generated by Django 4.1.3 on 2022-11-25 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_remove_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color')], max_length=10),
        ),
    ]
