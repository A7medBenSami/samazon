# Generated by Django 4.1.3 on 2022-11-25 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_stock_orderproduct_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adminnote',
            new_name='admin_note',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ip',
        ),
    ]
