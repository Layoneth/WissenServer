from django.conf.urls import patterns, url
from event.views import *
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = patterns('',
	url(r'^_eventos/$',  EventList.as_view(), name='event-list'),
	url(r'^_eventos/(?P<pk>\d+)/$', EventDetail.as_view(), name='event-detail'),
	url(r'^user/$',  UserList.as_view(), name='user-list'),
	url(r'^user/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
	url(r'^inscript/$',  InscripcionList.as_view(), name='inscripts-list'),
	url(r'^inscript/(?P<pk>\d+)/$', InscripcionDetail.as_view(), name='inscripts-detail'),

	url(r'^permisos/$',  PermissionList.as_view(), name='permisos-list'),
	url(r'^permisos/(?P<pk>\d+)/$', PermissionDetail.as_view(), name='permisos-detail'),

	url(r'^grupos/$',  GroupList.as_view(), name='groups-list'),
	url(r'^grupos/(?P<pk>\d+)/$', GroupDetail.as_view(), name='groups-detail'),

	url(r'^datosperfil/$',  DatosPerfil.as_view(), name='datosperfil'),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])