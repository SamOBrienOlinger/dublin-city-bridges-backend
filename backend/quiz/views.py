from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import QuizQuestion, QuizChoice, QuizAttempt
from .serializers import QuizQuestionSerializer, QuizAttemptSerializer

# ViewSet for Quiz Questions
class QuizQuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

# ViewSet for Quiz Attempts (Handle Submitting Scores)
class QuizAttemptViewSet(viewsets.ModelViewSet):
    queryset = QuizAttempt.objects.all()
    serializer_class = QuizAttemptSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def submit_score(self, request):
        user = request.user
        score = request.data.get('score')

        if score is not None:
            quiz_attempt = QuizAttempt.objects.create(user=user, score=score)
            return Response({'message': 'Score submitted successfully!', 'score': score})
        return Response({'message': 'Invalid score data'}, status=400)
