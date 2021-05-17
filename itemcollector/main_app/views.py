from django.shortcuts import render
from .models import Plant
from datetime import date

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def plants_index(request):
    plants = Plant.objects.order_by('id')
    current_date = date.today()
    for plant in plants:
        days_since = current_date - plant.date_watered
        plant.days = days_since.days
    return render(request, 'plants/index.html', { 'plants': plants})

def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    return render(request, 'plants/detail.html', { 'plant': plant })
