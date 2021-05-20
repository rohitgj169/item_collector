from datetime import date
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Plant, PlantForm, PlantEditForm, Pot
from .forms import FertilizerForm

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
    pots_not_in_use = Pot.objects.exclude(id__in = plant.pots.all().values_list('id'))
    fertilizer_form = FertilizerForm()
    return render(request, 'plants/detail.html', { 
        'plant': plant,
        'fertilizer_form': fertilizer_form,
        'pots': pots_not_in_use
    })

def add_fertilizer(request, plant_id):
    form = FertilizerForm(request.POST)
    if form.is_valid():
        new_entry = form.save(commit = False)
        new_entry.plant_id = plant_id
        new_entry.save()
    return redirect('detail', plant_id = plant_id)

def assoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id = plant_id).pots.add(pot_id)
    return redirect('detail', plant_id = plant_id)

def remove_pot(request, plant_id, pot_id):
    Plant.objects.get(id = plant_id).pots.remove(pot_id)
    return redirect('detail', plant_id = plant_id)

class PlantCreate(CreateView):
    model = Plant
    form_class = PlantForm

class PlantUpdate(UpdateView):
    model = Plant
    form_class = PlantEditForm

class PlantDelete(DeleteView):
    model = Plant
    success_url = '/plants/'

class PotList(ListView):
  model = Pot

class PotDetail(DetailView):
  model = Pot

class PotCreate(CreateView):
  model = Pot
  fields = '__all__'

class PotUpdate(UpdateView):
  model = Pot
  fields = ['name', 'color']

class PotDelete(DeleteView):
  model = Pot
  success_url = '/pots/'