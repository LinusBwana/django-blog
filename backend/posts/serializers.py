from rest_framework import serializers
from .models import Posts
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Posts
        fields = "__all__"