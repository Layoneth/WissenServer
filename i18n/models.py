from django.db import models
from event.models import Event


class Language(models.Model):
	""" La mayoría de los Idiomas del mundo """
	codigo = models.CharField(max_length=5) # (primary_key=True, max_length=5, unique=True)
	codigo2 = models.CharField(max_length=200, null=True, blank=True)
	descripcion = models.CharField(max_length=200, null=True, blank=True)
	original = models.CharField(max_length=200, null=True, blank=True)
	def __unicode__(self):
		return "%s - %s" % (self.codigo, self.original)



class LanguagesRegistered(models.Model):
	""" Idiomas en los que se traducirán los datos ingresados al sistema, como las disciplinas, preguntas, etc. """
	idioma = models.ForeignKey(Language) # (primary_key=True, max_length=5, unique=True)
	event = models.ForeignKey(Event) # Evento al que se registra este idioma.
	es_principal = models.BooleanField(default=False) # Solo es True si este es el idioma por defecto del sistema.
	def __unicode__(self):
		return "%s - %s" % (self.codigo, self.idioma.codigo)

