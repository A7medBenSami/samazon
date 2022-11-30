# Generated by Django 4.1.3 on 2022-11-19 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('image_id', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
        ),
        migrations.RemoveField(
            model_name='color',
            name='color',
        ),
        migrations.RemoveField(
            model_name='color',
            name='product',
        ),
        migrations.RemoveField(
            model_name='size',
            name='product',
        ),
        migrations.RemoveField(
            model_name='size',
            name='size',
        ),
        migrations.AddField(
            model_name='color',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='color',
            name='name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='size',
            name='code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='size',
            name='name',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Memory',
        ),
        migrations.AddField(
            model_name='variants',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.color'),
        ),
        migrations.AddField(
            model_name='variants',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
        migrations.AddField(
            model_name='variants',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.size'),
        ),
    ]
