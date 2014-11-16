from rest_framework import serializers
from event.models import Event



class LanguageSerializer(serializers.ModelSerializer):
	class Meta:
		model = Language


class LanguagesRegisteredSerializer(serializers.ModelSerializer):
	class Meta:
		model = LanguagesRegistered


