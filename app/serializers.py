from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import Group
from event.models import Event


class EntitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Entity



class CategoryTransSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryTranslate
	


class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
	


class _LevelTransSerializer(serializers.ModelSerializer):
	class Meta:
		model = LevelTranslate

class _EventSerializer(serializers.ModelSerializer):
	class Meta:
		model = Event

class LevelSerializer(serializers.ModelSerializer):
	traducciones = _LevelTransSerializer(required=False)
	event = _EventSerializer(required=False)
	class Meta:
		model = Level



class DisciplineTransSerializer(serializers.ModelSerializer):
	class Meta:
		model = DisciplineTranslate

class DisciplineSerializer(serializers.ModelSerializer):
	traducciones = DisciplineTransSerializer(required=False)
	event = _EventSerializer(required=False)
	class Meta:
		model = Discipline


class CategorySerializer(serializers.ModelSerializer):
	traducciones = CategoryTransSerializer(required=False)
	class Meta:
		model = Category
		#depth = 1
	



class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group

