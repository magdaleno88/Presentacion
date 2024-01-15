from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, CommentForm
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from .models import *

# Create your views here.


@csrf_protect
def Comments(request):
    
    comment_form = CommentForm()
    if request.method == 'POST':
       comment_form = CommentForm(request.POST)

       if comment_form.is_valid():
           new_comment = comment_form.save(commit=False)
           new_comment.user = request.user
           new_comment.save()
           return redirect('comments')
    else:
        comment_form = CommentForm()
    
    comments_all = Comment.objects.all()
    return render(request, 'comments.html',{
        'title':'Comentarios',
        'comment_form':comment_form,
        'comentarios': comments_all,
    })



def Register_page(request):

    register_form = RegisterForm()
    if request.method == "POST":
        register_form = RegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            usuario=register_form.save()    
            login(request, usuario)
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

def delete_comment(request, id):
    comentario = Comment.objects.get(pk=id)
    comentario.delete()

    return redirect('comments')