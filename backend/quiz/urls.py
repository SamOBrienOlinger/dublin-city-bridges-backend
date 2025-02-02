from django.urls import path
from .views import QuizQuestionList, SubmitQuizAttempt

urlpatterns = [
    path('api/quiz/questions/', QuizQuestionList.as_view(), name='quiz-questions'),
    path('api/quiz/attempt/', SubmitQuizAttempt.as_view(), name='submit-quiz-attempt'),
]
