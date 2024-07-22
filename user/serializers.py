from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["email", "username", "first_name", "last_name", "birthday", "liked_posts", "password"]
    read_only_fields = ("created_at", )
    extra_kwargs = {'password': {'write_only': True}}

  def create(self, data):
    user = User(
      email = data['email'],
      username = data['username'],
      first_name = data['first_name'],
      last_name = data['last_name'],
      birthday = data['birthday'],
    )
    user.set_password(data['password'])
    user.save()
    return user