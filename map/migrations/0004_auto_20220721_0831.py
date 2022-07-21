# Generated by Django 3.2 on 2022-07-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_maker'),
    ]

    operations = [
        migrations.RenameField(
            model_name='maker',
            old_name='description',
            new_name='description_paragraph1',
        ),
        migrations.AddField(
            model_name='maker',
            name='description_paragraph2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='maker',
            name='description_paragraph3',
            field=models.TextField(blank=True, null=True),
        ),
    ]
