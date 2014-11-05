from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from .models import Language, LanguagesRegistered


class LanguageViewSet(ModelViewSet):
	model = Language

class LanguagesRegisteredViewSet(ModelViewSet):
	model = LanguagesRegistered
