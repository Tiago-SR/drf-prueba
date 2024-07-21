from django.db import models
from django.utils import timezone


class User(models.Model):
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  birthday = models.DateField()
  created_at = models.DateTimeField(default=timezone.now)
  liked_posts = models.ManyToManyField('post.Post' ,related_name='liked_by', blank=True)
  def __str__(self):
    return f"{self.first_name} {self.last_name}"