from django.urls import path
from . import views

urlpatterns = [
    path('experience/', views.Experiences, name="experience"),
    
]