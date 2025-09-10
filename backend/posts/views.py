from warnings import filters
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework import viewsets, generics
from .serializers import PostSerializer
from .models import Posts
from .forms import PostForm
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


def posts_home(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Posts.objects.filter(
            Q(post_title__icontains=search_query) |
            Q(post_content__icontains=search_query) |
            Q(user__username__icontains=search_query)

        ).order_by('-posted_on')
    else:
        posts = Posts.objects.all().order_by('-posted_on')

    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    serialized_posts = PostSerializer(page_obj, many=True)
    return render(request, 'home.html', {'posts': serialized_posts.data, 
                                         'search_query': search_query,
                                         "page_obj": page_obj})

@login_required
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


@login_required
def edit_post(request, slug):
    post = get_object_or_404(Posts, slug=slug)

    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_details', slug=slug)
        form = PostForm(instance=post)
    return render(request, 'new_post.html', {
        'form': form,
        'edit_mode': True,
        'post': post,
    })