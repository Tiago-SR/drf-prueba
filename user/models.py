from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField()
  password = models.CharField(max_length=128)
  first_name = models.CharField(max_length=40)
  last_name = models.CharField(max_length=40)
  birthday = models.DateField()
  liked_posts = models.ManyToManyField('post.Post' ,related_name='liked_by', blank=True)
  def __str__(self):
    return f"{self.first_name} {self.last_name}"