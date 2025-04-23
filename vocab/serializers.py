from rest_framework import serializers
from .models import VocabularyWord, UserWordProgress

class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabularyWord
        fields = ['id', 'word', 'translation', 'example']

class UserWordProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWordProgress
        fields = ['id', 'word', 'known']
