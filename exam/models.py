from django.db import models
from app.models import Category
#from event.models import Event
from i18n.models import Language
from django.contrib.auth.models import User




class Exam(models.Model):
	""" 
	Información de un examen para luego relacionarlo con sus opciones.
	"""
	descripcion = models.CharField(max_length=200, null=True, blank=True)
	dirigido = models.BooleanField(default=False) # Si es dirigido, es una Final, si es False, es una eliminatoria.
	categoria_id = models.ForeignKey(Category)
	evento_id = models.ForeignKey('event.Event')
	duracion_preg = models.IntegerField(max_length=3, null=True, blank=True) # Duración de la pregunta si el examen es Dirigido y no la pregunta tiene duración asignada;
	duracion_exam = models.IntegerField(max_length=3, null=True, blank=True) # Duración del examen si es Independiente
	created_by = models.ForeignKey(User)
	created_at  = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True)


class Exam_Question(models.Model):
	""" 
	Registro de preguntas que tendrá un examen.
	"""
	exam = models.ForeignKey('Exam')
	preg = models.ForeignKey('Question')
	added_by = models.ForeignKey(User) # Usuario que registró la pregunta al examen
	

class Question(models.Model):
	""" 
	Codigo de las preguntas.
	"""
	pregunta = models.TextField('Exam', null=True, blank=True)
	duracion = models.IntegerField(max_length=3, null=True, blank=True) # (Seg)Duración de la pregunta si el examen es Dirigido
	correct = models.IntegerField(max_length=1) # Cual de las opciones será la correcta
	aleatorio = models.BooleanField(default=False) # Darle al programa la libertad de reordenar las opciones
	event = models.ForeignKey('event.Event')
	created_by = models.ForeignKey(User)
	created_at  = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True)



class QuestionTranslate(models.Model):
	""" 
	Traducción de las preguntas.
	"""
	enunciado = models.TextField('Exam', blank=True, null=True) # Aquí va el enunciado de la pregunta, puede ser null si hay una imagen
	preg = models.ForeignKey(Question) # Pregunta a la que se le está haciendo esta traducción
	img = models.FileField(max_length=400, null=True, blank=True, upload_to='images/questions') # Puede que la pregunta tenga imágenes con texto en diferentes idiomas
	idioma = models.ForeignKey(Language) # Idioma al que pertenece esta traducción.
	opc1 = models.TextField(blank=True, null=True)
	opc2 = models.TextField(blank=True, null=True)
	opc3 = models.TextField(blank=True, null=True)
	opc4 = models.TextField(blank=True, null=True)
	img1 = models.FileField(max_length=400, upload_to='images/questions', blank=True, null=True)
	img2 = models.FileField(max_length=400, upload_to='images/questions', blank=True, null=True)
	img3 = models.FileField(max_length=400, upload_to='images/questions', blank=True, null=True)
	img4 = models.FileField(max_length=400, upload_to='images/questions', blank=True, null=True)
	translated = models.BooleanField(default=False)
	created_by = models.ForeignKey(User)
	created_at  = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True)


class Question_Category(models.Model):
	""" 
	Indica en qué categorías se puede usar esta pregunta.
	"""
	preg = models.ForeignKey(Question)
	categoria = models.ForeignKey('app.Category') # Puede que la pregunta tenga imágenes con texto en diferentes idiomas
	assigned_by = models.ForeignKey(User)
	created_at  = models.DateTimeField(auto_now_add=True)
	udpated_at = models.DateTimeField(auto_now=True)




