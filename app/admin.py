from django.contrib import admin
from app.models import *


class EntityAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'logo', 'direccion', 'dirigente')
	list_filter = ('nombre', 'dirigente', 'event')
	search_fields = ('nombre', 'dirigente')

class DisciplineAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'event')
	list_filter = ('event',)
	search_fields = ('nombre', )

class DisciplineTranslateAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'discipline', 'idioma', 'descripcion')
	list_filter = ('idioma', 'translated')
	search_fields = ('nombre', 'discipline', 'descripcion')

class LevelAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'event')
	search_fields = ('nombre', )

class LevelTranstaleAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'level', 'descripcion', 'idioma')
	list_filter = ('idioma', 'translated')
	search_fields = ('nombre', 'level', 'descripcion')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'level', 'discipline')
	list_filter = ('nombre', 'level', 'discipline')
	search_fields = ('nombre',)
	ordering = ['nombre']

class CategoryTranslateAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'category', 'idioma', 'translated')
	list_filter = ('idioma', 'translated')
	search_fields = ('nombre', 'category', 'idioma')

class MessageAdmin(admin.ModelAdmin):
	list_display = ('user_from', 'user_to', 'msg', 'viewed')
	list_filter = ('user_from', 'user_to', 'msg')
	search_fields = ('user_from', 'user_to', 'msg')




admin.site.register(Entity, EntityAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(DisciplineTranslate, DisciplineTranslateAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(LevelTranslate, LevelTranstaleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CategoryTranslate, CategoryTranslateAdmin)
admin.site.register(Message, MessageAdmin)
