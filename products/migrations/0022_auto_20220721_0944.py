# Generated by Django 3.2 on 2022-07-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_auto_20220721_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='description',
            new_name='description_paragraph1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description_paragraph1',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_paragraph2',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description_paragraph3',
        ),
        migrations.AddField(
            model_name='category',
            name='description_paragraph2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='description_paragraph3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
