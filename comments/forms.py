from django import forms
from django.core import validators 

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

"Formulario de registro de un usuario en la base de datos"
class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget = forms.PasswordInput(
        attrs = {
            'class': 'register_field',
            'placeholder': 'Ingrese su contraseña',
            'id':'password1',
            'required':'required',
        }
    ))
    password2 = forms.CharField(label='Contraseña de confirmación', widget = forms.PasswordInput(
        attrs = {
            'class': 'register_field',
            'placeholder': 'Ingrese nuevamente su contraseña',
            'id':'password2',
            'required':'required',
        }
    ))
    class Meta:
        model = Usuario
        fields = ('email', 'username','nombres','apellidos', 'empleo','foto_perfil')
        widgets = {
            'nombres': forms.TextInput(
                attrs={
                    'class':'register_field',
                    'placeholder':'Ingrese su nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class':'register_field',
                    'placeholder':'Ingrese sus apellidos',
                }
            ),
            'empleo': forms.TextInput(
                attrs={
                    'class':'register_field',
                    'placeholder':'¿A que se dedica?',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class':'register_field',
                    'placeholder':'Ingrese su nombre de usuario',
                }
            )
        }
    def clean_password2(self):
        """
        Esta es la validacion de contraseña
        Este metodo valida que las contraseñas sean guardadas antes de ser encriptadas y guardadas
        en la base de datos y retorna la contraseña valida 

        Excepciones:
        -Validation error, cuando no son iguales marca error 
        """
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden')
        return password2

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']