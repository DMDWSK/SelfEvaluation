from django.db import models
from django.contrib.auth.models import User


class UserAnswers(models.Model):
    class Meta:
        db_table = "UserAnswers"
        ordering = ['id']
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey('allactions.Questions',on_delete=models.CASCADE)
    answer = models.BooleanField(default=False)
    grade = models.ForeignKey('allactions.Grades',on_delete=models.CASCADE)
