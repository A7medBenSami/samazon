# Generated by Django 4.1.3 on 2022-11-25 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(editable=False),
        ),
    ]
