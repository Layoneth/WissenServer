from django.contrib import admin
from event.models import *

# Register your models here.

class Participant_LevelAdmin(admin.ModelAdmin):
	pass


admin.site.register(Event)
admin.site.register(Participant_Level, Participant_LevelAdmin)
admin.site.register(Inscription)
admin.site.register(User_Event)
admin.site.register(Test)
admin.site.register(Answer)
admin.site.register(Bug)
