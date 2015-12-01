from django.db import models
from django.conf import settings

class Usuario(models.Model):
    nick = models.OneToOneField(settings.AUTH_USER_MODEL)
    nombre = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    photo = models.ImageField(upload_to='profiles', blank=True, null=True)

    def __unicode__(self):
        return self.nick
