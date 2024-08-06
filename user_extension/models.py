from django.db import models
from django.contrib.auth.models import User


class Extension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.TextField(null=True)