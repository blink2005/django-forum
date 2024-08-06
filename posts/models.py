from django.db import models

class Post(models.Model):
    category = models.TextField()
    title = models.TextField()
    description = models.TextField()
    id_creator = models.TextField(null=True)