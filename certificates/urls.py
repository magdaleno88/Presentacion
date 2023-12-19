from django.urls import path
from . import views

urlpatterns = [
    path('certifications/', views.certifications, name="certifications")
]
