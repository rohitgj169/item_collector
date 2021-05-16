from django.shortcuts import render
from .models import Item

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def items_index(request):
    items = Item.objects.order_by('id')
    return render(request, 'items/index.html', { 'items': items })

def items_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    return render(request, 'items/detail.html', { 'item': item })