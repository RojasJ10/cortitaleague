#encoding:utf-8
from django.db import models
from django.conf import settings


class Equipo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    entrenador = models.CharField(max_length=30)
    escudo = models.ImageField(upload_to='imagenes', verbose_name='fotoescudo',  blank=True)
    VICTORIA = 3;
    EMPATE = 1;
    DERROTA = 0;
    resultado = (
        (VICTORIA, 3),
        (EMPATE, 1),
        (DERROTA, 0),
    )
    resultado = models.IntegerField(choices=resultado)
    gf = models.IntegerField(default=0)
    gc = models.IntegerField(default=0);
    dg = models.IntegerField(default=0);
    pg = models.IntegerField(default=0);
    pe = models.IntegerField(default=0);
    pp = models.IntegerField(default=0);

    def __unicode__(self):
        return self.nombre
# class Formulario(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['nick', 'nombre', 'apellido', 'email']
