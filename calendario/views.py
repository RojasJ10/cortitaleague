from calendario.models import Partido
from django.shortcuts import render_to_response

def lista_partidos(request):
    partidos = Partido.objects.all().order_by('fecha')
    return render_to_response('lista_partidos.html', {'lista':partidos})
