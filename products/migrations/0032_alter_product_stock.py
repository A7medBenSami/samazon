# Generated by Django 4.1.3 on 2022-11-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_alter_product_default_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
    ]