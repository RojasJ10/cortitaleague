from principal.models import Equipo, Jugador
from django.shortcuts import render_to_response

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render_to_response('lista_equipos.html', {'lista':equipos})

def lista_jugadores(request):
    jugadores = Jugador.objects.all()
    return render_to_response('lista_jugadores.html', {'lista':jugadores})
