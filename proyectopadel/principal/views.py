from django.shortcuts import render, render_to_response, get_object_or_404
from principal.models import Jugador, Pareja, Partido, Pista, Arbitro
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

def inicio(request):
	return render_to_response("inicio.html", context_instance=RequestContext(request))

def portada(request):
	return render_to_response("portada.html", context_instance=RequestContext(request))

def index(request):
	return render_to_response("index.html", context_instance=RequestContext(request))

def lista_jugadores(request):
	jugadores = Jugador.objects.all()
	return render_to_response('lista_jugadores.html',{'jugadores':jugadores},context_instance=RequestContext(request))

def jugador(request, nombre):
	x = Jugador.objects.get(nombre=nombre)
	return render_to_response('jugador.html',{'y':x}, context_instance=RequestContext(request))

def lista_arbitros(request):
	arbitros = Arbitro.objects.all()
	return render_to_response("lista_arbitros.html",{'datos':arbitros}, context_instance=RequestContext(request))

def lista_partidos(request):
	partidos = Partido.objects.order_by('fecha')
	return render_to_response("lista_partidos.html",{'datos':partidos}, context_instance=RequestContext(request))

def partido(request, idpartido):
	x = Partido.objects.get(idpartido=idpartido)
	return render_to_response('partido.html',{'y':x}, context_instance=RequestContext(request))

def lista_pistas(request):
	pistas = Pista.objects.all()
	return render_to_response("lista_pistas.html",{'datos':pistas}, context_instance=RequestContext(request))

def lista_parejas(request):
	parejas = Pareja.objects.all()
	return render_to_response("lista_parejas.html",{'datos':parejas}, context_instance=RequestContext(request))

def ranking(request):
	parejas = Pareja.objects.order_by('-puntos')	#Poniendo el - delante, hacemos orden inverso
	return render_to_response("ranking.html",{'datos':parejas}, context_instance=RequestContext(request))
