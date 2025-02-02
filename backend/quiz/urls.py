from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuizQuestionViewSet, QuizAttemptViewSet

# Set up the router for the Quiz endpoints
router = DefaultRouter()

# Register the viewsets for questions and attempts
router.register(r'questions', QuizQuestionViewSet)
router.register(r'attempts', QuizAttemptViewSet)

# Define the URL patterns for the API
urlpatterns = [
    path('api/', include(router.urls)),
]
