from dataclasses import fields
import imp
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UsuarioCriarForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'cpf', 'nome', 'password1', 'password2']