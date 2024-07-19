from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment

# Create your views here.
@csrf_exempt
def posts(request):
  match request.method:
    case 'GET':
      return get(request)
    case 'POST':
      return post(request)


def get(request):
  posts = Post.objects.all().values()
  return HttpResponse(posts)

def post(request):
  title = request.POST['title']
  author = request.POST['author']
  content = request.POST['content']
  post = Post.objects.create(title = title, author = author, content = content)

  return HttpResponse(post)