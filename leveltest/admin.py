from django.contrib import admin
from .models import VocabularyTestResult, ListeningTestResult, LevelTestResult, VocabularyWord, ListeningQuestion


admin.site.register(VocabularyTestResult)
admin.site.register(ListeningTestResult)
admin.site.register(LevelTestResult)
admin.site.register(VocabularyWord)
admin.site.register(ListeningQuestion)