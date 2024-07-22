from django.db import models
from django.utils import timezone

class Comment(models.Model):
  post = models.ForeignKey('post.Post', related_name="comments", on_delete=models.CASCADE)
  author = models.ForeignKey('user.User', related_name='comments', on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  def __str__(self):
    return "{self.post.title}"