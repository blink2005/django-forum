from django.db import models


class UserPost(models.Model):
    title = models.TextField()
    user = models.TextField()