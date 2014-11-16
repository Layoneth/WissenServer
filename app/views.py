from django.shortcuts import render

from app.models import *
from event.serializers import UserSerializer
from .serializers import *
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import obtain_auth_token


def principal(request):
	#t = loader.get_template('pag.html')
	return render(request, 'index.html')
	#return HttpResponse(serialize("json", Nota.objects.all()))
	#return Response(serialize("json", Nota.objects.all()))



# Creamos los ModelViewSets para el API de djangorestframework
class EntityViewSet(ModelViewSet):
	model = Entity

class DisciplineViewSet(ModelViewSet):
	model = Discipline

class DisciplineTransViewSet(ModelViewSet):
	model = DisciplineTranslate

class MessageViewSet(ModelViewSet):
	model = Message


class LevelViewSet(ModelViewSet):
	model = Level

class LevelTransViewSet(ModelViewSet):
	model = LevelTranslate




class NivelList(generics.ListCreateAPIView):
	model = Level
	serializer_class = LevelSerializer

class NivelDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Level
	serializer_class = LevelSerializer



class DisciplineList(generics.ListCreateAPIView):
	model = Discipline
	serializer_class = DisciplineSerializer

class DisciplineDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Discipline
	serializer_class = DisciplineSerializer




class CategoryViewSet(ModelViewSet):
	model = Category
	serializer_class = CategorySerializer

class CategoryTransViewSet(ModelViewSet):
	model = CategoryTranslate





class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders it's content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def autenticar(request):
	#myDict = dict(request.POST.iterlists())
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			#login(request, user)
			token = Token.objects.get_or_create(user=user)
			print("Token adquirido: ", obtain_auth_token(request).data)
			serializer = UserSerializer(user)
			serializer.data['token'] = obtain_auth_token(request).data
			return JSONResponse(serializer.data)
			#tex = "Usuario %s logueado!" % username
			#return HttpResponse(tex)
			# Redirect to a success page.
			"""
		else:
			# Return a 'disabled account' error message
	else:
		# Return an 'invalid login' error message.
"""
	texDev = "Usuario %s a loguear!" % username
	return HttpResponse(texDev)




def vlogout(request):
	logout(request)
	return HttpResponse('El usuario ha cerrado sesión.')

