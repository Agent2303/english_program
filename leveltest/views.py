from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import VocabularyTestResult, VocabularyWord, ListeningTestResult, ListeningQuestion,LevelTestResult
from .serializers import VocabularyTestResultSerializer, VocabularyWordSerializer,LevelTestResultSerializer,ListeningTestResultSerializer, ListeningQuestionSerializer


# Vocabulary Test Savollarini olish
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def start_vocabulary_test(request):
    # Random 10 ta so‘zni tanlab olish
    words = VocabularyWord.objects.order_by('?')[:10]
    serializer = VocabularyWordSerializer(words, many=True)
    return Response(serializer.data)

# Vocabulary Testni yuborish (natijalar)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def submit_vocabulary_test(request):
    answers = request.data.get('answers', [])  # [{word_id: X, answer: "olma"}]
    correct = 0

    for ans in answers:
        try:
            word = VocabularyWord.objects.get(id=ans['word_id'])
            if word.translation.strip().lower() == ans['answer'].strip().lower():
                correct += 1
        except VocabularyWord.DoesNotExist:
            pass

    # Darajani aniqlash
    if correct <= 3:
        level = "Beginner"
    elif correct <= 5:
        level = "Elementary"
    elif correct <= 7:
        level = "Intermediate"
    else:
        level = "Upper-Intermediate"

    # Natijalarni saqlash
    VocabularyTestResult.objects.create(user=request.user, score=correct, level=level)

    # Feedback
    return Response({
        "score": correct,
        "level": level,
        "message": f"Your score is {correct} points, indicating a {level} level. Keep practicing!"
    })



# Listening Test Savollarini olish
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def start_listening_test(request):
    # Random 10 ta savolni tanlab olish
    questions = ListeningQuestion.objects.order_by('?')[:10]
    serializer = ListeningQuestionSerializer(questions, many=True)
    return Response(serializer.data)

# Listening Testni yuborish (natijalar)
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def submit_listening_test(request):
    answers = request.data.get('answers', [])  # [{question_id: X, answer: "olma"}]
    correct = 0

    for ans in answers:
        try:
            question = ListeningQuestion.objects.get(id=ans['question_id'])
            if question.correct_answer.strip().lower() == ans['answer'].strip().lower():
                correct += 1
        except ListeningQuestion.DoesNotExist:
            pass

    # Darajani aniqlash
    if correct <= 2:
        level = "Beginner"
    elif correct <= 4:
        level = "Intermediate"
    else:
        level = "Advanced"

    # Natijalarni saqlash
    ListeningTestResult.objects.create(user=request.user, score=correct, level=level)

    # Feedback
    return Response({
        "score": correct,
        "level": level,
        "message": f"You have scored {correct} points in the listening test, your level is {level}. Great job!"
    })


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_test_results(request):
    vocabulary_results = VocabularyTestResult.objects.filter(user=request.user)
    listening_results = ListeningTestResult.objects.filter(user=request.user)
    level_results = LevelTestResult.objects.filter(user=request.user)

    vocabulary_serializer = VocabularyTestResultSerializer(vocabulary_results, many=True)
    listening_serializer = ListeningTestResultSerializer(listening_results, many=True)
    level_serializer = LevelTestResultSerializer(level_results, many=True)

    return Response({
        'vocabulary_results': vocabulary_serializer.data,
        'listening_results': listening_serializer.data,
        'level_results': level_serializer.data,
    })
