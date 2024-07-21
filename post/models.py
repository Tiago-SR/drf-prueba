from django.db import models
from django.utils import timezone

class Post(models.Model):
  title = models.CharField(max_length=40)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey('user.User', related_name='posts', on_delete=models.CASCADE)
  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
  author = models.ForeignKey('user.User', related_name='comments', on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return "{self.post.title}"