from django.forms import ModelForm
from django import forms
from .models import Usuario

class Formulario(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nick', 'nombre', 'apellido', 'email']
