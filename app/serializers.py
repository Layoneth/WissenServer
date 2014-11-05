from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import Group


class EntitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Entity



class CategoryTransSerializer(serializers.ModelSerializer):
	class Meta:
		model = CategoryTranslate
	


class MessageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Message
	


class LevelTransSerializer(serializers.ModelSerializer):
	class Meta:
		model = LevelTranslate

class LevelSerializer(serializers.ModelSerializer):
	traducciones = LevelTransSerializer(required=False)
	class Meta:
		model = Level



class DisciplineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Discipline
	
class DisciplineTransSerializer(serializers.ModelSerializer):
	class Meta:
		model = DisciplineTranslate


class CategorySerializer(serializers.ModelSerializer):
	traducciones = CategoryTransSerializer(required=False)
	class Meta:
		model = Category
		#depth = 1
	
		

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group

