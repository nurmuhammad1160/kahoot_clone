from django.contrib import admin
from .models import GameSession, GameParticipant, ParticipantAnswer


# Register your models here.
admin.site.register(GameSession, admin.ModelAdmin)
admin.site.register(GameParticipant, admin.ModelAdmin)
admin.site.register(ParticipantAnswer, admin.ModelAdmin)