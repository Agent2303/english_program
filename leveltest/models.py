from django.db import models
from django.contrib.auth.models import User
from vocab.models import VocabularyWord

class VocabularyTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    level = models.CharField(max_length=50)  # Example levels: Beginner, Intermediate, etc.
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.level} - {self.score} points"

class ListeningTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    level = models.CharField(max_length=50)  # Example levels: Beginner, Intermediate, Advanced
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.level} - {self.score} points"


class LevelTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    level = models.CharField(max_length=50)  # Example levels: Beginner, Elementary, Intermediate, Advanced
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Level: {self.level} - {self.score} points"


class VocabularyWord(models.Model):
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.word} - {self.translation}"


class ListeningQuestion(models.Model):
    audio_url = models.URLField(max_length=200)  # URL to the audio file
    question_text = models.CharField(max_length=255)  # The question text
    choices = models.JSONField()  # A list of choices
    correct_answer = models.CharField(max_length=255)  # The correct answer

    def __str__(self):
        return f"Question: {self.question_text} - Correct Answer: {self.correct_answer}"
