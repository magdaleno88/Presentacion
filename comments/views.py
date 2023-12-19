from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def Comments(request):

    return render(request, 'comments.html',{
        'title':'Comentarios'
    })

def Register_page(request):

    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado correctamente')
            return redirect('comments')

    return render(request,'register_page.html',{
        'title':'Registro',
        'register_form': register_form
    })

def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Bienvenido')
            return redirect('comments')
        else:
            messages.warning(request, 'No te has podido identificar')
    
    return render(request, 'login_page.html',{
        'title':'Identificate bro'
    })

def Logout_user(request):
    logout(request)
    return redirect('comments')