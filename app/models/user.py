from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    point_earned = models.IntegerField(default=0)
