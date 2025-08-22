from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Posts

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

def posts_home(request):
    posts = Posts.objects.all().order_by('-posted_on')
    serialized_posts = PostSerializer(posts, many=True)
    return render(request, 'home.html', {'posts': serialized_posts.data})

def post_details(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    serialized_post = PostSerializer(post)
    return render(request, 'post_page.html', {'post': serialized_post.data})