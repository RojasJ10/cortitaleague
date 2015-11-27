from django.db import models

class Equipo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    entrenador = models.CharField(max_length=30)
    escudo = models.ImageField(upload_to='imagenes', verbose_name='fotoescudo',  blank=True)

    def __unicode__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    PORTERO = 'PO'
    DEFENSA = 'DF'
    MEDIO = 'ME'
    DELANTERO = 'DL'
    posicion = (
        (PORTERO, 'PO'),
        (DEFENSA, 'DF'),
        (MEDIO, 'ME'),
        (DELANTERO, 'DL'),
    )
    posicion = models.CharField(max_length=2, choices=posicion)
    foto = models.ImageField(upload_to='imagenes', verbose_name='fotojugador',  blank=True)
    equipo = models.ForeignKey(Equipo)
    class Meta:
        verbose_name_plural = 'Jugadores'

    def __unicode__(self):
        return self.nombre
