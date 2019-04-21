from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    follwers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_followers_user")
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_followings_user")