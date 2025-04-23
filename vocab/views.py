from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import VocabularyWord, UserWordProgress
from .serializers import VocabularySerializer, UserWordProgressSerializer
import random

class VocabularyListCreateView(generics.ListCreateAPIView):
    queryset = VocabularyWord.objects.all()
    serializer_class = VocabularySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def random_words(request):
    words = list(VocabularyWord.objects.all())
    sample = random.sample(words, min(len(words), 5))
    serializer = VocabularySerializer(sample, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def mark_word_known(request):
    word_id = request.data.get('word_id')
    known = request.data.get('known', True)
    word = VocabularyWord.objects.get(id=word_id)
    obj, created = UserWordProgress.objects.update_or_create(
        user=request.user,
        word=word,
        defaults={'known': known}
    )
    return Response({'message': 'Updated successfully'})