# Generated by Django 3.2.3 on 2021-05-17 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_plant_date_watered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='date_watered',
            field=models.DateField(auto_now_add=True),
        ),
    ]
