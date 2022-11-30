# Generated by Django 4.1.3 on 2022-11-26 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_alter_coupons_options_coupons_minimum'),
        ('order', '0005_order_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coupons.coupons'),
        ),
    ]