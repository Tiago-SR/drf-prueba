from .models import Comment
from rest_framework import viewsets
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer