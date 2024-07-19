from django.db import models
from django.utils import timezone

class Post(models.Model):
  title = models.CharField(max_length=40)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  author = models.CharField(max_length=40)


class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
  author = models.CharField(max_length=40)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)