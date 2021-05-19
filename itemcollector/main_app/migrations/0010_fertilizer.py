# Generated by Django 3.2.3 on 2021-05-19 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_plant_water_interval'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('A', 'Soil Conditioner'), ('B', 'Stage 1 - Nitro'), ('C', 'Stage 2 - Grow'), ('D', 'Stage 3 = Bloom')], default='A', max_length=1)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.plant')),
            ],
        ),
    ]