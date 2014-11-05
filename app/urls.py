from app.views import *
from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = patterns('',
	url(r'^niveles/$',  NivelList.as_view(), name='levels-list'),
	url(r'^niveles/(?P<pk>\d+)/$', NivelDetail.as_view(), name='levels-detail'),

)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])