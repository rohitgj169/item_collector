from django import forms
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

TYPES = (
    ('A', 'Soil Conditioner'),
    ('B', 'Stage 1 - Nitro'),
    ('C', 'Stage 2 - Grow'),
    ('D', 'Stage 3 - Bloom')
)

class DateInput(forms.DateInput):
    input_type = 'date'

class Pot(models.Model):
    name = models.CharField(max_length = 100)
    color = models.CharField(max_length = 20)
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pots_detail', kwargs = {'pk' : self.id})

class Plant(models.Model):
    alias= models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    sun = models.CharField(max_length=100)
    water = models.CharField(max_length=100)
    humidity = models.CharField(max_length=100)
    water_interval = models.IntegerField()
    date_watered = models.DateField()
    pots = models.ManyToManyField(Pot)
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'plant_id': self.id})

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['alias', 'name', 'type', 'sun', 'water', 'humidity', 'water_interval', 'date_watered', 'description']
        widgets = {
            'date_watered': DateInput()
        }

class PlantEditForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['sun', 'water', 'humidity', 'water_interval', 'date_watered', 'description']
        widgets = {
            'date_watered': DateInput()
        }

class Fertilizer(models.Model):
    date = models.DateField('fertilize date')
    type = models.CharField(
        max_length = 1,
        choices = TYPES,
        default = TYPES[0][0]
        )

    plant = models.ForeignKey(Plant, on_delete = models.CASCADE)

    def __str__(self):
        return f"Add {self.get_type_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']