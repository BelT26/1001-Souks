# Generated by Django 3.2 on 2022-04-19 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20220419_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='maker',
            new_name='maker1',
        ),
    ]
