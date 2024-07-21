from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer
from post.models import Post

def checkPost(post_id):
  try:
    post_id = int(post_id)
    post = Post.objects.get(pk=post_id)
    return post
  except Post.DoesNotExist:
    return Response({'detail': 'El ID del Post no existe.'}, status=status.HTTP_404_NOT_FOUND)
  except:
    return Response({'detail': 'El ID del Post debe ser numero entero.'}, status=status.HTTP_400_BAD_REQUEST)
  
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer

  @action(detail=True, methods=['post'], url_path='like/(?P<post_id>[^/.]+)')
  def like_post(self, request, pk=None, post_id=None):
    post = checkPost(post_id)
    if not isinstance(post, Post):
      return post
    user: User = self.get_object()
    user.liked_posts.add(post)
    user.save()
    return Response({'detail': 'Like creado correctamente',}, status=status.HTTP_200_OK)
  
  @action(detail=True, methods=['post'], url_path='unlike/(?P<post_id>[^/.]+)')
  def unlike_post(self, request, pk=None, post_id=None):
    post = checkPost(post_id)
    if not post:
      return post 
    user: User = self.get_object()
    user.liked_posts.remove(post)
    user.save()
    return Response({'detail': 'Like eliminado correctamente'})