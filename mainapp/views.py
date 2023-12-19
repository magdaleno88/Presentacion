from django.shortcuts import render
from certificates.models import *

# Create your views here.
def index(request):

    certificates = Certificate.objects.all()
    data=[]
    for a in range(0,4,1):
        data.append(certificates[a])
    return render(request, 'mainapp/index.html',{
        'title':'Inicio',
        'certificates':data
    })


def about(request):

    return render(request, 'mainapp/about.html',{
        'title':'Sobre mi'
    })


def experience(request):

    return render(request, 'mainapp/experience.html',{
        'title':'Experiencia laboral'
    })