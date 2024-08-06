from django.db import models

class Comment(models.Model):
    message = models.TextField()
    post_id = models.TextField()
    id_creator = models.TextField(null=True)
