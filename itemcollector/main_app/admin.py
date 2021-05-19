from django.contrib import admin
from .models import Fertilizer, Plant, Pot

# Register your models here.

admin.site.register(Plant)
admin.site.register(Fertilizer)
admin.site.register(Pot)