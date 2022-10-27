from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.forms import models
from django.db import models
from django.forms.fields import ImageField

from .models import Profile
from django.core import validators
from django.utils.translation import gettext_lazy as _, ngettext_lazy

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label= 'Correo Electrónico',
        required=True,
    )

    username = forms.CharField(
        max_length=40, 
        required=True,
        label='Nombre de Usuario'
    )
    
    password1 = forms.CharField(
        label = "Contraseña",
        required=True
    )
    password2 = forms.CharField(
        label = "Confirmar Contraseña",
        required=True,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Correo Electrónico',
        required=True
    )

    username = forms.CharField(
        required=True,
        label='Nombre de Usuario',
    )

    
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(
        label = 'Foto de perfil'
    )

    description = forms.CharField(
        label = 'Sobre ti (Máximo 600 caracteres)',
        required=False,
        max_length=600
    )
    
    class Meta:
        model = Profile
        fields = ['description', 'image']

"""
class BuyingForm(forms.ModelForm):
    nombre = forms.CharField(
        label= 'Nombre',
        required=True,
    )

    apellido = forms.CharField(
        max_length=40, 
        required=True,
        label='Apellido'
    )
    
    tajetanumero = forms.CharField(
        label = "Número de la tarjeta",
        required=True
    )
    cvv = forms.CharField(
        label = "Código de seguridad (CVV)",
        required=True,
    )
    
    date = forms.DateField(
        label = "Fecha de expiración",
        required=True,
    )

    class Meta:
        model = User
        fields = ['nombre', 'apellido', 'tarjetanumero', 'cvv', 'date']
"""