from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from usuarios.forms import JugadorForm, ParejaForm, PartidoForm, ArbitroForm, PistaForm, UserForm
from django.template import RequestContext, loader
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from principal.models import Jugador, Pareja, Partido, Pista, Arbitro
from django.db.models import Q

@login_required(login_url='/ingresar')
def nuevo_jugador(request):
	if request.method=='POST':
		formulario = JugadorForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/jugadores')
	else:
		formulario = JugadorForm()
	return render_to_response('jugadorform.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def nueva_pareja(request):
	if request.method=='POST':
		formulario = ParejaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/parejas')
	else:
		formulario = ParejaForm()
	return render_to_response('parejaform.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def nuevo_partido(request):
	if request.method=='POST':
		formulario = PartidoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/partidos')
	else:
		formulario = PartidoForm()
	return render_to_response('partidoform.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def nuevo_arbitro(request):
	if request.method=='POST':
		formulario = ArbitroForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/arbitros')
	else:
		formulario = ArbitroForm()
	return render_to_response('arbitroform.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def nueva_pista(request):
	if request.method=='POST':
		formulario = PistaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/pistas')
	else:
		formulario = PistaForm()
	return render_to_response('pistaform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_usuario(request):
	if request.method=='POST':
		formulario=UserCreationForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/index')
	else:
		formulario=UserCreationForm()
	return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/index')
	if request.method=='POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/index')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('ingresar.html', {'formulario':formulario}, context_instance = RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
	usuario = request.user
	return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))


def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/')

@login_required(login_url='/ingresar')
def editar_perfil(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect('/privado')
    else:
        user_form = UserForm(instance=request.user)
    return render_to_response('editar_perfil.html', { 'user_form': user_form }, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def editar_jugador(request, nombre):
	jugador = Jugador.objects.get(nombre=nombre)
	if request.method=='POST':
		form = JugadorForm(request.POST, instance = jugador)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/jugadores')
	else:
		form = JugadorForm(instance = jugador)
	return render_to_response('editar_jugador.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def editar_partido(request, idpartido):
	partido = Partido.objects.get(idpartido=idpartido)
	if request.method=='POST':
		form = PartidoForm(request.POST, instance = partido)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/partidos')
	else:
		form = PartidoForm(instance = partido)
	return render_to_response('editar_partido.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def editar_pareja(request, idpareja):
	pareja = Pareja.objects.get(idpareja=idpareja)
	if request.method=='POST':
		form = ParejaForm(request.POST, instance = pareja)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/parejas')
	else:
		form = ParejaForm(instance = pareja)
	return render_to_response('editar_pareja.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def editar_pista(request, idpista):
	pista = Pista.objects.get(idpista=idpista)
	if request.method=='POST':
		form = PistaForm(request.POST, instance = pista)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/pistas')
	else:
		form = PistaForm(instance = pista)
	return render_to_response('editar_pista.html', {'form':form}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def editar_arbitro(request, numero_colegiado):
	arbitro = Arbitro.objects.get(numero_colegiado=numero_colegiado)
	if request.method=='POST':
		form = ArbitroForm(request.POST, instance = arbitro)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/arbitros')
	else:
		form = ArbitroForm(instance = arbitro)
	return render_to_response('editar_arbitro.html', {'form':form}, context_instance=RequestContext(request))
