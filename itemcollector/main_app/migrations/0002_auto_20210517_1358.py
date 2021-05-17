# Generated by Django 3.2.3 on 2021-05-17 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('sun', models.CharField(max_length=100)),
                ('water', models.CharField(max_length=100)),
                ('humidity', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
