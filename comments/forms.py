from django import forms
from django.core import validators 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']