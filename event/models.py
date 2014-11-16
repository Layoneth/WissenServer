from django.db import models
from django.contrib.auth.models import User




class Event(models.Model):
	""" 
	Configuración del evento a realizar
	"""
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=400, null=True, blank=True)
	exam_actual = models.IntegerField(default=0) # Se relaciona con 'exam.Exam' pero no 
	with_pay = models.BooleanField(default=True) # ¿En este evento se harán pagos por las inscripciones? True=Sí se harán pagos. False=No se harán pagos.
	precio1 = models.IntegerField(default=2000) # Precios para las iscripciones a categorías.
	precio2 = models.IntegerField(default=3000)
	precio3 = models.IntegerField(default=4000)
	precio4 = models.IntegerField(default=5000)
	precio5 = models.IntegerField(default=6000)
	precio6 = models.IntegerField(default=7000)
	allow_pay_less = models.BooleanField(default=True) # Permitir pago modificados por el asesor para cobrar diferente del precio estipulado por el sistema.
	allow_cross_users = models.BooleanField(default=True) # Este evento permite usuarios de otros eventos?
	enable_public_chat = models.BooleanField(default=True) # Indica si el chat público estará habilitado
	enable_private_chat = models.BooleanField(default=True) # Indica que los usuario se pueden enviar mensajes privados.
	def __str__(self):
		return "%s - %s" % (self.nombre, self.descripcion)
	class Meta:
		verbose_name = "evento"
		verbose_name_plural = "eventos"


class Participant_Level(models.Model):
	""" 
	Los niveles a los que un usuario puede registrar categorías
	"""
	nivel = models.ForeignKey('app.Level')
	user = models.ForeignKey(User, related_name='participant_levels')
	class Meta:
		verbose_name = "asignación de nivel a participante"
		verbose_name_plural = "asignaciones de niveles a participantes"


class Inscription(models.Model):
	""" 
	Categorías en las que se registrará a un usuario para que haga los exámenes
	"""
	categoria = models.ForeignKey('app.Category')
	user = models.ForeignKey(User, related_name='inscriptions')
	allowed = models.BooleanField(default=True) # Cuando el participante haga un test, cambia a False, pero un asesor puede darle otra oportunidad, volviendolo True de nuevo.
	signed_by = models.ForeignKey(User, related_name='inscription_signed_by') # Usuario que inscribió al participante
	created_at  = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True) 
	def __str__(self):
		return '%s - %s' % (self.categoria.nombre, self.user.first_name)
	class Meta:
		verbose_name = "inscripción"
		verbose_name_plural = "inscripciones"



class User_Event(models.Model):
	""" 
	Eventos a los que se ha inscrito al usuario, es decir que un usuario puede estar registrado en varios eventos.
	"""
	user = models.ForeignKey(User, related_name='users_signed')
	event = models.ForeignKey(Event, related_name='events') # Cuando el participante haga un test, cambia a False, pero un asesor puede darle otra oportunidad, volviendolo True de nuevo.
	pagado = models.IntegerField(max_length=7, default=0) # Dinero pagado por el usuario en este evento.
	a_paz = models.BooleanField(default=False) # Dinero pagado por el usuario en este evento.
	signed_by = models.ForeignKey(User, related_name='event_signed_by') # Usuario que inscribió al participante
	created_at  = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True) 
	def __str__(self):
		return '%s - %s' % (self.event.nombre, self.user.first_name)
	class Meta:
		verbose_name = "Asignación de evento a usuario"
		verbose_name_plural = "asignaciones de eventos a usuarios"


class Test(models.Model):
	""" 
	Examen respondido de un usuario en una inscripción
	El Test hecho por un participante solo cuenta si está habilitado (enable=True) de lo contrario
	este Test se tomará como si fuera de prueba o de error y no contará para los puntajes.
	"""
	inscripcion = models.ForeignKey(Inscription) # La inscrición me dirá qué usuario es quien respondión este Test
	exam = models.ForeignKey('exam.Exam') # Examen a responder en este Test
	enable = models.BooleanField(default=True) # Cuando sea False, no contará para los resultados o puestos.
	deleted = models.BooleanField(default=False) # Con el Test solo haremos borrados suaves (soft delete) por seguridad
	created_at  = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return '%s %s' % (self.exam, self.inscripcion)
	class Meta:
		verbose_name = "test"
		verbose_name_plural = "test(exámenes respondidos)"


class Answer(models.Model):
	""" 
	Respuesta de un usuario a una regunta de un Test.
	"""
	preg = models.ForeignKey('exam.Question')
	test = models.ForeignKey(Test)
	letter_responded = models.CharField(max_length=1, default='A')
	tiempo = models.IntegerField(max_length=3) # (Seg)Tiempo que duró respondiendo la pregunta
	created_at  = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True)
	class Meta:
		verbose_name = "respuesta"
		verbose_name_plural = "respuestas"
	


class Bug(models.Model):
	""" 
	Problemas que un usuario reporta sobre una pregunta
	"""
	description = models.CharField(max_length=400, null=True, blank=True) # El usuario explica qué problema tiene
	preg = models.IntegerField(null=True, blank=True) # Pregunta sobre la cual se reporta el problema
	reported_by = models.ForeignKey('auth.User', related_name='bug_reported_by') # Usuario que reportó el bug
	fixed = models.BooleanField(default=False) # ¿Ya fue arreglado el bug?
	fixed_by = models.ForeignKey('auth.User') # Usuario que arregló el bug
	created_at  = models.DateTimeField(auto_now_add=True) # Momento en que se reportó
	udpated_at = models.DateTimeField(auto_now=True) # Se puede decir que esta modificación dice cuando fue arreglado el bug, pero no es de fiar.
	class Meta:
		verbose_name = "bug"
		verbose_name_plural = "bugs del sistema"





# Extenderé las columnas de User, ya que la tabla User de Django no tiene todas los campos que necesitamos.
User.add_to_class('cell', models.CharField(max_length=200, null=True, blank=True)) # Número de celular
User.add_to_class('direccion', models.CharField(max_length=400, null=True, blank=True))
User.add_to_class('img', models.ImageField(max_length=200, null=True, blank=True)) # Foto del usuario.
User.add_to_class('evento', models.IntegerField(max_length=5, default=0)) # Evento en el que participará, si es cero, estará en cualquier evento.
User.add_to_class('connected', models.BooleanField(default=False)) # Es True mientras está logueado, y False cuando se sale del sistema.
User.add_to_class('signed_by', models.IntegerField(null=True, blank=True)) # Usuario que inscribió esta persona. Debería ser Foraneo, pero me complica al registrar el primero.
User.add_to_class('idioma_system', models.IntegerField(max_length=3, default=0)) # Si es cero, se usará el idioma por defecto, el que "es_principal=True"
User.add_to_class('idioma_preg', models.IntegerField(max_length=3, default=0)) # Related with 'i18n.LanguagesRegistered'


# Atributos muchos a muchos, osea, no son reales en la tabla.
# Solo servirán desde la versión 1.7 de Django
#User.add_to_class('inscriptions', models.ManyToManyField(Inscription)) # Noooo
#User.add_to_class('categorias', models.ManyToManyField('app.Category', through='Inscription', through_fields=('user_id', 'categoria_id')))
#User.add_to_class('niveles', models.ManyToManyField('app.Level', through='Participant_Level', through_fields=('user_id', 'nivel_id')))


"""
class Perfil(User):
	# Datos extras para los usuarios
	categorias = models.ManyToManyField('app.Category', through='Inscription', through_fields=('user_id', 'categoria_id'))
	niveles = models.ManyToManyField('app.Level', through='Participant_Level', through_fields=('user_id', 'nivel_id'))
"""		




