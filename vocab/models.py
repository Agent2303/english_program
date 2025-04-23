from django.db import models
from django.contrib.auth.models import User

class VocabularyWord(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    example = models.TextField(blank=True)

    def __str__(self):
        return self.word

class UserWordProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(VocabularyWord, on_delete=models.CASCADE)
    known = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'word')

