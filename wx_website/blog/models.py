from django.db import models

# Create your models here.
class BlogsPost(models.Model):
    title = models.CharField(max_length = 150)  # blog title
    body = models.TextField()                   # blog content
    timestamp = models.DateTimeField()          # blog create time
