from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from user.models import User
from user.serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer

class LoginView(APIView):
  authentication_classes = () # Se requiere para no tener un error de csrf
  def post(self, request):
    username = request.data.get('username', None)
    password = request.data.get('password', None)
    user = authenticate(username=username, password=password)

    if user:
      login(request, user)
      token, created = Token.objects.get_or_create(user=user)
      return Response({'detail': 'Login successfully', 'token': token.key}, status=status.HTTP_200_OK)
    return Response({'detail': 'Username or Password incorrect'}, status=status.HTTP_404_NOT_FOUND)