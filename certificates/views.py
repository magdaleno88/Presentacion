from django.shortcuts import render
from certificates.models import *
# Create your views here.
def certifications(request):

    certificates = Certificate.objects.all()
    apollo=2
    duplas=[]
    for cer in range(1,len(certificates)+1,1):
        if cer%2!=0 and cer == len(certificates):
            duplas.append([certificates[cer-1],""])
        elif cer%2!=0:
            apollo=cer
        else:
            duplas.append([certificates[apollo-1], certificates[cer-1]])


    return render(request, 'certifications.html',{
        'title':'Certificados',
        'certificates':duplas
    })