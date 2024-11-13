from django.contrib import admin
from .models import Game, Question, Answer, QuestionFile

# Register your models here.
admin.site.register(Game, admin.ModelAdmin)
admin.site.register(Question, admin.ModelAdmin)
admin.site.register(Answer, admin.ModelAdmin)
admin.site.register(QuestionFile, admin.ModelAdmin)
