# Generated by Django 3.2 on 2022-04-19 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_maker'),
        ('products', '0009_product_multibuy_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='maker1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.maker'),
        ),
    ]
