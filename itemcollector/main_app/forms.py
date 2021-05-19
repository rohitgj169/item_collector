from django.forms import ModelForm
from .models import Fertilizer

class FertilizerForm(ModelForm):
    class Meta:
        model = Fertilizer
        fields = ['date', 'type']