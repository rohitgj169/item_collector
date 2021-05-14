from django.shortcuts import render
from django.http import HttpResponse

class Item:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

items = [
    Item('OneTeebs', 'tech', 'hold tonnes of data'),
    Item('Studler', 'stationery', 'mightier than a sword'),
    Item('Klipz', 'personal care', 'cuts both ways'),

]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello<h1>')

def about(request):
    return render(request, 'about.html')

def items_index(request):
    return render(request, 'items/index.html', { 'items': items })