from django.db import models
from django.urls import reverse
# Create your models here.

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

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs = {'plant_id': self.id})
