from django.db import models
from principal.models import Equipo

class Partido(models.Model):
    local = models.ForeignKey(Equipo, related_name='partidos_de_local')
    visitante = models.ForeignKey(Equipo, related_name='partidos_de_visitante')
    fecha = models.DateField()

    def __unicode__(self):
         return u"%s - %s (%s)" % (self.local, self.visitante, self.fecha)

        # return unicode(self.local) + 'vs' + unicode(self.visitante) + '' str(self.fecha)
