from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Posts

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer