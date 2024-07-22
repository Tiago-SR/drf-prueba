from rest_framework import serializers
from .models import Post
from comment.serializers import CommentToPost

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = "__all__"
    read_only_fields = ("created_at", )

class PostDetailSerializer(serializers.ModelSerializer):
  comments = CommentToPost(many=True, read_only=True)
  class Meta:
    model = Post
    fields = "__all__"
    read_only_fields = ("created_at", )