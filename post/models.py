from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
  title = models.CharField(max_length=20)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  author = models.CharField(max_length=100)


class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
  author = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)