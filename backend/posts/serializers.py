from rest_framework import serializers
from .models import Posts
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    # posted_on = serializers.DateTimeField(format="%d %B %Y at %I:%M %p", read_only=True)
    user = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Posts
        fields = "__all__"