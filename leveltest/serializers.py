from rest_framework import serializers
from .models import VocabularyTestResult, ListeningTestResult, LevelTestResult, VocabularyWord, ListeningQuestion

# Vocabulary Test Result Serializer
class VocabularyTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabularyTestResult
        fields = ['user', 'score', 'level', 'date']

# Listening Test Result Serializer
class ListeningTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningTestResult
        fields = ['user', 'score', 'level', 'date']

# Level Test Result Serializer
class LevelTestResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelTestResult
        fields = ['user', 'score', 'level', 'date']

# Vocabulary Word Serializer
class VocabularyWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabularyWord
        fields = ['id', 'word', 'translation']

# Listening Question Serializer
class ListeningQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningQuestion
        fields = ['id', 'audio', 'question_text', 'choices', 'correct_answer']
