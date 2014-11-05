from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from .models import *


class ExamViewSet(ModelViewSet):
	model = Exam

class Exam_QuestionViewSet(ModelViewSet):
	model = Exam_Question

class QuestionViewSet(ModelViewSet):
	model = Question

class QuestionTransViewSet(ModelViewSet):
	model = QuestionTranslate
	
class Question_CategoryViewSet(ModelViewSet):
	model = Question_Category

