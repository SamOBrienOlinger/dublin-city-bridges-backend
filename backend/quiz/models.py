from django.db import models
from django.contrib.auth.models import User

class QuizQuestion(models.Model):
    prompt = models.CharField(max_length=500)
    choices = models.JSONField()  # Store choices as a JSON list
    answer = models.CharField(max_length=1)  # 'a', 'b', 'c', or 'd'

    def __str__(self):
        return self.prompt

class UserQuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attempt by {self.user.username} with score {self.score}"

