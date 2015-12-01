from principal.models import Equipo
from django.shortcuts import render_to_response

def lista_equipos(request):
    equipos = Equipo.objects.all()
    return render_to_response('lista_equipos.html', {'lista':equipos})
#
# def lista_usuarios(request):
#     usuarios = Usuario.objects.all()
#     return render_to_response('lista_usuarios.html', {'lista':usuarios})

def login(request):
    return render_to_response('login.html')
