from django.shortcuts import render
from .serializers import CommentSerializer
from .models import Comments
from rest_framework import viewsets

# Create your views here.
class CommentViewSets(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer