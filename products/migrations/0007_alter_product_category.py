# Generated by Django 4.1.3 on 2022-11-17 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_images_product_images_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(limit_choices_to={'catparent__isnull': True}, on_delete=django.db.models.deletion.CASCADE, related_name='pro_category', to='products.category'),
        ),
    ]
