#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from principal import views as principalviews
from usuarios import views as usuariosviews
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('principal.urls')),  #podríamos poner tambien r^principal/ y en el localhost 127.../principal
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
    {'document_root':settings.MEDIA_ROOT,}
    ),
    url(r'^inicio/','principal.views.inicio'),
    url(r'^index/','principal.views.index'),
    url(r'^$/','principal.views.portada'),
    url(r'^jugadores/$','principal.views.lista_jugadores'),
    url(r'^arbitros/$','principal.views.lista_arbitros'),
    url(r'^partidos/$','principal.views.lista_partidos'),
    url(r'^pistas/$','principal.views.lista_pistas'),
    url(r'^parejas/$','principal.views.lista_parejas'),
    url(r'^jugadorform/','usuarios.views.nuevo_jugador'),
    url(r'^parejaform/','usuarios.views.nueva_pareja'),
    url(r'^partidoform/','usuarios.views.nuevo_partido'),
    url(r'^arbitroform/','usuarios.views.nuevo_arbitro'),
    url(r'^pistaform/','usuarios.views.nueva_pista'),
    url(r'^nuevousuario$', 'usuarios.views.nuevo_usuario'),
    url(r'^ingresar/$', 'usuarios.views.ingresar'),
    url(r'^privado/$','usuarios.views.privado'),
    url(r'^cerrar/$', 'usuarios.views.cerrar'),
    url(r'^editarperfil/$','usuarios.views.editar_perfil'),
    url(r'^jugadores/detalle/(?P<nombre>[\w|\W]+)$', 'principal.views.jugador'),
    url(r'^partidos/detalle/(?P<idpartido>[\w|\W]+)$', 'principal.views.partido'),
    url(r'^ranking/','principal.views.ranking'),
    url(r'^jugadores/editarjugador/(?P<nombre>[\w|\W]+)$', 'usuarios.views.editar_jugador'),
    url(r'^partidos/editarpartido/(?P<idpartido>[\w|\W]+)$', 'usuarios.views.editar_partido'),
    url(r'^parejas/editarpareja/(?P<idpareja>[\w|\W]+)$', 'usuarios.views.editar_pareja'),
    url(r'^pistas/editarpista/(?P<idpista>[\w|\W]+)$', 'usuarios.views.editar_pista'),
    url(r'^arbitros/editararbitro/(?P<numero_colegiado>[\w|\W]+)$', 'usuarios.views.editar_arbitro'),
)
