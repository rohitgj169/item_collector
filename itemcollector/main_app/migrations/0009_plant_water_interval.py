# Generated by Django 3.2.3 on 2021-05-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_plant_date_watered'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='water_interval',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
