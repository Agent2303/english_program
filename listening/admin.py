from django.contrib import admin
from .models import ListeningTask, ListeningAnswer, ListeningQuestion


admin.site.register(ListeningTask)
admin.site.register(ListeningAnswer)
admin.site.register(ListeningQuestion)


