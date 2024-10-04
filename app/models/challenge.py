from django.db import models
from .award import Award
from .user import User


class Challenge(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    point = models.IntegerField()
    Award = models.ForeignKey(Award, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ChallengeItem(models.Model):
    Challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_to_display = models.DateTimeField()

    def __str__(self):
        return self.title


class ChallengeTransaction(models.Model):
    ChallengeItem = models.ForeignKey(ChallengeItem, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.User} - {self.ChallengeItem.title} - {self.created_at}"