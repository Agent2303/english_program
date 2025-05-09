from rest_framework import serializers
from .models import ListeningTask, ListeningQuestion, ListeningAnswer

class ListeningQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningQuestion
        fields = ['id', 'question_text']

class ListeningTaskSerializer(serializers.ModelSerializer):
    questions = ListeningQuestionSerializer(many=True, read_only=True)

    class Meta:
        model = ListeningTask
        fields = ['id', 'title', 'audio', 'transcript', 'questions']

class ListeningAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningAnswer
        fields = ['question', 'answer']
