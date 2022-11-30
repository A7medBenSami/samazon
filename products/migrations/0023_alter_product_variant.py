# Generated by Django 4.1.3 on 2022-11-25 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_alter_product_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color')], max_length=10),
        ),
    ]