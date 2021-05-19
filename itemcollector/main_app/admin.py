from django.contrib import admin
from .models import Fertilizer, Plant

# Register your models here.

admin.site.register(Plant)
admin.site.register(Fertilizer)