from app.views import *
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = patterns('',
	url(r'^_niveles/$',  NivelList.as_view(), name='levels-list'),
	url(r'^_niveles/(?P<pk>\d+)/$', NivelDetail.as_view(), name='levels-detail'),
	url(r'^_disciplinas/$',  NivelList.as_view(), name='disc-list'),
	url(r'^_disciplinas/(?P<pk>\d+)/$', NivelDetail.as_view(), name='disc-detail'),

)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])