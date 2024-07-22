from .models import Post
from rest_framework import viewsets
from .serializers import PostSerializer, PostDetailSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  
  # El metodo get_serializer_class determina que 'accion' se debe llevar a cabo 
  def get_serializer_class(self):
    # 'retrieve' es cuando se consulta un elemento especifico
    if self.action == 'retrieve':
      return PostDetailSerializer
    return PostSerializer