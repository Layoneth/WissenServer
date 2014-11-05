from django.db import models
from i18n.models import Language
from event.models import Event


class Entity(models.Model):
	""" Entidades de los participantes, colegios, iglesias, paises, etc. """
	nombre = models.CharField(max_length=200)
	logo = models.CharField(max_length=600, null=True, blank=True)
	direccion = models.CharField(max_length=200, null=True, blank=True)
	dirigente = models.CharField(max_length=200, null=True, blank=True)
	celular = models.CharField(max_length=200, null=True, blank=True)
	event = models.ForeignKey(Event, null=True, blank=True)
	def __unicode__(self):
		return '%s - id_evento: %d' % self.nombre, self.event.id


class Discipline(models.Model):
	""" 
	Nombre de las ciencias de las preguntas 
	ejemplos:
		- Matemáticas, Español, etc.
		- Apocalipsis, Daniel, etc.
	"""
	nombre = models.CharField(max_length=100, null=True, blank=True)
	event = models.ForeignKey(Event, null=True, blank=True)
	def __unicode__(self):
		return "%s - %s" % (self.nombre, self.event.nombre)


class DisciplineTranslate(models.Model):
	""" 
	Traducción registrada para las diciplinas
	"""
	discipline = models.ForeignKey('Discipline', related_name='traducciones') # Disciplina a la que pertenece esta traducción
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200, null=True, blank=True)
	idioma = models.ForeignKey(Language)
	translated = models.BooleanField(default=False)


class Level(models.Model):
	""" 
	Dificultades de las olimpiadas 
	ejemplos: 
		- facil, medio, dificil, etc.
		- A, B, C, etc. 
		- niños, adultos, etc.
	"""
	nombre = models.CharField(max_length=100, null=True, blank=True)
	event = models.ForeignKey(Event, null=True, blank=True)
	def __unicode__(self):
		return "%s - %s" % (self.nombre, self.event.nombre)


class LevelTranslate(models.Model):
	""" 
	Traducción registrada para los niveles
	"""
	level = models.ForeignKey('Level', related_name='traducciones') # Nivel a la que pertenece esta traducción
	nombre = models.CharField(max_length=100)
	descripcion = models.CharField(max_length=200, null=True, blank=True)
	idioma = models.ForeignKey(Language)
	translated = models.BooleanField(default=False)
	def __unicode__(self):
		return "%s - %s" % (self.idioma, self.nombre)


class Category(models.Model):
	""" 
	Relación entre Displine y Level
	"""
	nombre = models.CharField(max_length=200, null=True, blank=True)
	level = models.ForeignKey('Level')
	discipline = models.ForeignKey('Discipline')
	event = models.ForeignKey(Event, null=True, blank=True)
	def __unicode__(self):
		return self.nombre


class CategoryTranslate(models.Model):
	""" 
	Traducciones de las categorías.
	"""
	category = models.ForeignKey(Category, related_name='traducciones')
	nombre = models.CharField(max_length=200, null=True, blank=True)
	idioma = models.ForeignKey(Language)
	translated = models.BooleanField(default=False)

	

class Message(models.Model):
	""" 
	Mensaje enviado por un usuario a otro.
	"""
	user_from = models.ForeignKey('auth.User') # Usuario que envia el mensaje.
	user_to = models.IntegerField(max_length=5, null=True, blank=True) # Usuario al que se envia el msg, pero puede ser null si desea enviarlo a todos los presentes, por lo tanto no lo dejo Foraneo.
	msg = models.TextField() # No debe estar vacío.
	viewed = models.DateTimeField(null=True, blank=True) # Indica que ya ha sido abierto o leído.
	soft_viewed = models.DateTimeField(null=True, blank=True) # Indica que el receptor ya vió el mensaje en la lista de mensajes, no indica que lo halla leido.
	reported = models.BooleanField(default=False) # Si el mensaje es público(user_to es igual a cero) otro usuario puede reportarlo!
	reported_by = models.IntegerField(max_length=5, null=True, blank=True) # Usuario que reportó el mensaje como inapropiado
	reported_at = models.DateTimeField(null=True, blank=True) # FechaHora en que se reportó
	created_at  = models.DateTimeField(auto_now_add=True) # Momento en que se envió el mensaje.

		