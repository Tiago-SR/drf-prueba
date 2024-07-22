from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = "__all__"
    read_only_fields = ("created_at", )

class CommentToPost(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['content', 'author', 'created_at']
    read_only_fields = ("created_at", )