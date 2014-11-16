from django.contrib import admin
from exam.models import *

admin.site.register(Exam)
admin.site.register(Exam_Question)
admin.site.register(Question)
admin.site.register(QuestionTranslate)
admin.site.register(Question_Category)
