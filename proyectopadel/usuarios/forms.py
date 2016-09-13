#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Arbitro, Jugador, Pareja, Partido, Pista
from django.contrib.auth.models import User

class JugadorForm(ModelForm):
	class Meta:
		model = Jugador

class ParejaForm(ModelForm):
    class Meta:
        model = Pareja

class PartidoForm(ModelForm):
    class Meta:
        model = Partido

class ArbitroForm(ModelForm):
    class Meta:
        model = Arbitro

class PistaForm(ModelForm):
    class Meta:
        model = Pista

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
