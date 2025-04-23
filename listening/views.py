from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import ListeningTask, ListeningQuestion, ListeningAnswer
from .serializers import ListeningTaskSerializer, ListeningAnswerSerializer

class ListeningTaskListView(generics.ListCreateAPIView):
    queryset = ListeningTask.objects.all()
    serializer_class = ListeningTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListeningTaskDetailView(generics.RetrieveAPIView):
    queryset = ListeningTask.objects.all()
    serializer_class = ListeningTaskSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def submit_answer(request):
    serializer = ListeningAnswerSerializer(data=request.data)
    if serializer.is_valid():
        question = serializer.validated_data['question']
        user_answer = serializer.validated_data['answer']
        correct_answer = (question.correct_answer or "").strip().lower()
        user_input = (user_answer or "").strip().lower()
        is_correct = correct_answer == user_input

        ListeningAnswer.objects.create(
            user=request.user,
            question=question,
            answer=user_answer,
            is_correct=is_correct
        )
        return Response({"correct": is_correct})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
