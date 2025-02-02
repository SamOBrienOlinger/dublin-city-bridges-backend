from rest_framework import serializers
from .models import QuizQuestion, UserQuizAttempt

class QuizQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizQuestion
        fields = ['id', 'prompt', 'choices', 'answer']

class UserQuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserQuizAttempt
        fields = ['user', 'score', 'date']
