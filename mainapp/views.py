from django.shortcuts import render
from certificates.models import *
from experience.models import *
from comments.models import *

# Create your views here.
def index(request):

    certificates = Certificate.objects.all()
    commentss = Comment.objects.all()
    experience = Experience.objects.latest('end_date')
    data_certificates=[]
    data_comments = []
    for a in range(0,4,1):
        data_certificates.append(certificates[a])
        data_comments.append(commentss[a])
    return render(request, 'mainapp/index.html',{
        'title':'Inicio',
        'certificates':data_certificates,
        'comentarios':data_comments,
        'experiencia':experience
    })


def about(request):

    return render(request, 'mainapp/about.html',{
        'title':'Sobre mi'
    })
