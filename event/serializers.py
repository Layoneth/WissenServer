from event.models import *
#from app.models import LevelSerializer

from app.serializers import CategorySerializer
from django.contrib.auth.models import Group, User, Permission
from i18n.models import Language, LanguagesRegistered
from rest_framework import serializers




class _LanguagesRegisteredSerializer(serializers.ModelSerializer):
	class Meta:
		model = LanguagesRegistered


class EventSerializer(serializers.ModelSerializer):
	languages = _LanguagesRegisteredSerializer(required=False)
	class Meta:
		model = Event



class InscripcionSerializer(serializers.ModelSerializer):
	#categoria = CategorySerializer(required=False)
	class Meta:
		model = Inscription
		#fields = ('user', )	

class PermissionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Permission

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group

class ParticipantLevelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Participant_Level

class UserSerializer(serializers.ModelSerializer):
	inscriptions = InscripcionSerializer(required=False)
	participant_levels = ParticipantLevelSerializer(required=False)
	#user_permissions = PermissionSerializer(required=False)
	#groups = GroupSerializer(required=False)

	class Meta:
		model = User
		#fields = ('username', 'first_name', 'last_name', 'email', 'inscriptions')
		#lookup_field = 'slug'
		#write_only_fields = ('password',)
		#depth = 1



