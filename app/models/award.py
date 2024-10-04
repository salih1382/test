from django.db import models
from .user import User


class Award(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class AwardTransaction(models.Model):
    Award = models.ForeignKey(Award, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.User} - {self.Award.name} - {self.created_at}"