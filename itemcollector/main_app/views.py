from datetime import date
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Plant, PlantForm, PlantEditForm, Pot
from .forms import FertilizerForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def plants_index(request):
    plants = Plant.objects.filter(user = request.user)
    current_date = date.today()
    for plant in plants:
        days_since = current_date - plant.date_watered
        plant.days = days_since.days
    return render(request, 'plants/index.html', { 'plants': plants})

@login_required
def plants_detail(request, plant_id):
    plant = Plant.objects.get(id=plant_id)
    pots_not_in_use = Pot.objects.filter(user = request.user).exclude(id__in = plant.pots.all().values_list('id'))
    fertilizer_form = FertilizerForm()
    return render(request, 'plants/detail.html', { 
        'plant': plant,
        'fertilizer_form': fertilizer_form,
        'pots': pots_not_in_use
    })

@login_required
def add_fertilizer(request, plant_id):
    form = FertilizerForm(request.POST)
    if form.is_valid():
        new_entry = form.save(commit = False)
        new_entry.plant_id = plant_id
        new_entry.save()
    return redirect('detail', plant_id = plant_id)

@login_required
def assoc_pot(request, plant_id, pot_id):
    Plant.objects.get(id = plant_id).pots.add(pot_id)
    return redirect('detail', plant_id = plant_id)

@login_required
def remove_pot(request, plant_id, pot_id):
    Plant.objects.get(id = plant_id).pots.remove(pot_id)
    return redirect('detail', plant_id = plant_id)

class PlantCreate(LoginRequiredMixin, CreateView):
    model = Plant
    form_class = PlantForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PlantUpdate(LoginRequiredMixin, UpdateView):
    model = Plant
    form_class = PlantEditForm

class PlantDelete(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = '/plants/'

class PotList(LoginRequiredMixin, ListView):
  model = Pot
  def get_queryset(self):
      return Pot.objects.filter(user = self.request.user)

class PotDetail(LoginRequiredMixin, DetailView):
  model = Pot

class PotCreate(LoginRequiredMixin, CreateView):
  model = Pot
  fields = '__all__'

class PotUpdate(LoginRequiredMixin, UpdateView):
  model = Pot
  fields = ['name', 'color']

class PotDelete(LoginRequiredMixin, DeleteView):
  model = Pot
  success_url = '/pots/'

class SignUp(CreateView):
  form_class = UserCreationForm
  success_url ='/'
  template_name = 'registration/signup.html'

  def form_valid(self, form):
    super().form_valid(form)
    login(self.request, form.instance)
    return redirect(SignUp.success_url)

