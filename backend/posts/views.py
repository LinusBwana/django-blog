from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Posts
from .forms import PostForm
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

def posts_home(request):
    posts = Posts.objects.all().order_by('-posted_on')
    serialized_posts = PostSerializer(posts, many=True)
    return render(request, 'home.html', {'posts': serialized_posts.data})

def post_details(request, slug):
    post = get_object_or_404(Posts, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_details', slug=slug)
    form = CommentForm()

    serialized_post = PostSerializer(post)
    return render(request, 'post_page.html', {'post': serialized_post.data,'form': form})

@login_required
def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    
    return render(request, 'new_post.html', {'form': form})


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    if request.user == post.user:
        post.delete()
        return redirect('home')
    return redirect('post_details', slug=post.slug)