from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('plants/', views.plants_index, name = 'index'),
    path('plants/<int:plant_id>/', views.plants_detail, name = 'detail'),
    path('plants/create/', views.PlantCreate.as_view(), name = 'plants_create'),
    path('plants/<int:pk>/update/', views.PlantUpdate.as_view(), name = 'plants_update'),
    path('plants/<int:pk>/delete/', views.PlantDelete.as_view(), name = 'plants_delete'),
    path('plants/<int:plant_id>/add_fertilizer', views.add_fertilizer, name = 'add_fertilizer'),
    path('pots/', views.PotList.as_view(), name = 'pots_index'),
    path('pots/<int:pk>/', views.PotDetail.as_view(), name = 'pots_detail'),
]
