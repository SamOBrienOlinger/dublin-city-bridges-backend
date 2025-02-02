from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import QuizQuestion, UserQuizAttempt
from .serializers import QuizQuestionSerializer, UserQuizAttemptSerializer
from rest_framework import status

class QuizQuestionList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        questions = QuizQuestion.objects.all()
        serializer = QuizQuestionSerializer(questions, many=True)
        return Response(serializer.data)

class SubmitQuizAttempt(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        score = request.data.get('score')

        # Save the quiz attempt
        quiz_attempt = UserQuizAttempt.objects.create(user=user, score=score)

        serializer = UserQuizAttemptSerializer(quiz_attempt)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
