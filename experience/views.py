from django.shortcuts import render
from .models import *

# Create your views here.
def Experiences(request):

    experiencias = Experience.objects.all()
    
    return render(request, 'experiences.html',{
        'title':'Experiencia aboral',
        'experiencias':experiencias
    })