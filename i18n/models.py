from django.db import models
from event.models import Event


class Language(models.Model):
	""" La mayoría de los Idiomas del mundo """
	codigo = models.CharField(max_length=5) # (primary_key=True, max_length=5, unique=True)
	codigo2 = models.CharField(max_length=200, null=True, blank=True)
	descripcion = models.CharField(max_length=200, null=True, blank=True)
	original = models.CharField(max_length=200, null=True, blank=True)
	def __str__(self):
		return "%s - %s" % (self.codigo, self.original)
	class Meta:
		verbose_name = "idioma"
		verbose_name_plural = "idiomas"



class LanguagesRegistered(models.Model):
	""" Idiomas en los que se traducirán los datos ingresados al sistema, como las disciplinas, preguntas, etc. """
	idioma = models.ForeignKey(Language, related_name='registradas') # (primary_key=True, max_length=5, unique=True)
	event = models.ForeignKey(Event, related_name='languages') # Evento al que se registra este idioma.
	es_principal = models.BooleanField(default=False) # Solo es True si este es el idioma por defecto del sistema.
	def __str__(self):
		return "%s - %s" % (self.codigo, self.idioma.codigo)
	class Meta:
		verbose_name = "idioma registrado"
		verbose_name_plural = "idiomas registrados"

