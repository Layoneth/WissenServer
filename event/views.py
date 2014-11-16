from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from django.contrib.auth.models import *
from .serializers import *




class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	model = User
	#write_only_fields = ('password',)  # Note: Password field is write-only
	lookup_field = 'id'



class EventList(generics.ListCreateAPIView):
	model = Event
	serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Event
	serializer_class = EventSerializer


class UserList(generics.ListCreateAPIView):
	model = User
	serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	model = User
	serializer_class = UserSerializer



class InscripcionList(generics.ListCreateAPIView):
	model = Inscription
	serializer_class = InscripcionSerializer

class InscripcionDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Inscription
	serializer_class = InscripcionSerializer



class PermissionList(generics.ListCreateAPIView):
	model = Permission
	serializer_class = PermissionSerializer

class PermissionDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Permission
	serializer_class = PermissionSerializer





class GroupList(generics.ListCreateAPIView):
	model = Group
	serializer_class = GroupSerializer

class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Group
	serializer_class = GroupSerializer






class DatosPerfil(APIView):
	"""
	Para regresar los datos de un usuario conectado gracias a su token en la cookie.
	"""
	model = User
	def get(self, request, format=None):
		# No funciona.
		#if(request.user == 'AnonymousUser'):
		#	return Response('{"respuesta": "Debes loguarte para ver tu perfil."}')

		serializer = UserSerializer(request.user)
		return Response(serializer.data)
		



class EventViewSet(ModelViewSet):
	model = Event


class Participant_LevelViewSet(ModelViewSet):
	model = Participant_Level


class InscriptionViewSet(ModelViewSet):
	model = Inscription
	


class TestViewSet(ModelViewSet):
	model = Test


class AnswerViewSet(ModelViewSet):
	model = Answer


class BugViewSet(ModelViewSet):
	model = Bug


