# encoding: utf-8
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Jugador(models.Model):
	drive = 'Drive'
	reves = 'Reves'
	POSICION = (
    (drive, 'Drive'),
    (reves, 'Reves'),
    )
	posicion = models.CharField(choices=POSICION, default='Versátil', max_length=10)
	nombre = models.CharField(max_length=50, verbose_name='Nombre')
	dni = models.CharField(max_length=9, unique=True, verbose_name='DNI')
	edad = models.IntegerField()
	altura = models.FloatField()
	foto = models.ImageField(upload_to='fotos/', verbose_name='Imagen', default='Sin foto')
	def __unicode__(self):
		return self.nombre

class Pareja(models.Model):
	jugador1 = models.ForeignKey('Jugador', related_name='jugador1')
	jugador2 = models.ForeignKey('Jugador', related_name='jugador2')
	idpareja = models.IntegerField(unique=True, default='0')
	entrenador = models.CharField(max_length=50)
	victorias = models.IntegerField(default='0')
	derrotas = models.IntegerField(default='0')
	puntos = models.IntegerField(default='0')
	def __unicode__(self):
		return unicode(self.jugador1) + ' / ' + unicode(self.jugador2)

class Partido(models.Model):
	pareja1 = models.ForeignKey('Pareja', related_name='pareja1')
	pareja2 = models.ForeignKey('Pareja', related_name='pareja2')
	fecha = models.DateTimeField(help_text='dd/mm/aaaa hh:mm:ss')
	pista = models.ForeignKey('Pista', related_name='pista')
	arbitro = models.ForeignKey('Arbitro')
	idpartido = models.IntegerField(unique=True, default='0')
	set1p1 = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(0)], default='0')
	set1p2 = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(0)], default='0')
	set2p1 = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(0)], default='0')
	set2p2 = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(0)], default='0')
	set3p1 = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(0)], default='0')
	set3p2 = models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(0)], default='0')
	def __unicode__(self):
		return unicode(self.pareja1) + ' vs ' + unicode(self.pareja2) +  ' ' + unicode(self.pista) + ' (' + unicode(self.pista.ciudad) + ') ' + str(self.fecha)


class Pista (models.Model):
	nombre_pista = models.CharField(max_length='50', default='Por determinar')
	ciudad = models.CharField(max_length='50')
	idpista = models.IntegerField(unique=True, default='0')
	foto = models.ImageField(upload_to='fotos/', verbose_name='Imagen', default='Sin foto')
	def __unicode__(self):
		return self.nombre_pista


class Arbitro (models.Model):
	nombre_arbitro = models.CharField(max_length='50')
	numero_colegiado = models.CharField(max_length='12', unique=True)
	foto = models.ImageField(upload_to='fotos/', verbose_name='Imagen', default='Sin foto')
	def __unicode__(self):
		return self.nombre_arbitro
