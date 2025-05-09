from django.db import models
from django.contrib.auth.models import User

class ListeningTask(models.Model):
    title = models.CharField(max_length=255)
    audio = models.FileField(upload_to='audio/')  # yoki FileField agar yuklansa
    transcript = models.TextField(blank=True)

    def __str__(self):
        return self.title

class ListeningQuestion(models.Model):
    task = models.ForeignKey(ListeningTask, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=100)

class ListeningAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(ListeningQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
