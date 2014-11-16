from django.contrib import admin
from i18n.models import *


class LanguageAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'codigo2', 'descripcion', 'original')
	search_fields = ('codigo', 'descripcion', 'original')

admin.site.register(Language, LanguageAdmin)
admin.site.register(LanguagesRegistered)
