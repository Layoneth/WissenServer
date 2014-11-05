from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter

from event import urls as eventurls
from app import urls as appurls
from exam import urls as examurls
from i18n import urls as i18nurls

from app.views import *
from event.views import *
from exam.views import *
from i18n.views import *


from django.contrib import admin
admin.autodiscover()


router = DefaultRouter()
# app
router.register(r'entidades', EntityViewSet)
router.register(r'disciplinas', DisciplineViewSet)
router.register(r'disciplinatrans', DisciplineTransViewSet)
#router.register(r'niveles', LevelViewSet)
router.register(r'nivelestrans', LevelTransViewSet)
router.register(r'categorias', CategoryViewSet)
router.register(r'categoriastrans', CategoryTransViewSet)
router.register(r'mensajes', MessageViewSet)
# event
router.register(r'users', UserViewSet)
router.register(r'eventos', EventViewSet)
router.register(r'nivel_participante', Participant_LevelViewSet)
router.register(r'inscripciones', InscriptionViewSet)
router.register(r'test', TestViewSet)
router.register(r'respuestas', AnswerViewSet)
router.register(r'bug', BugViewSet)
# exam
router.register(r'exam', ExamViewSet)
router.register(r'pregunta_exam', Exam_QuestionViewSet)
router.register(r'preguntas', QuestionViewSet)
router.register(r'preguntastrans', QuestionTransViewSet)
router.register(r'preguntas_categoria', Question_CategoryViewSet)
# i18n
router.register(r'idiomas', LanguageViewSet)
router.register(r'idiomastrans', LanguagesRegisteredViewSet)




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WissenSystemBackend.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(eventurls)),
    url(r'^api/', include(appurls)),
    url(r'^api/', include(examurls)),
    url(r'^api/', include(i18nurls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include(router.urls)),
    url(r'^api/login', autenticar),
    url(r'^api/logout/?', vlogout),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'), # Para saber qué token se le ha asignado a un usuario.

)
