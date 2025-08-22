from rest_framework import serializers
from .models import Comments

class CommentSerializer(serializers.ModelSerializer):
    # commented_on = serializers.DateTimeField(format="%d %B %Y at %I:%M %p", read_only=True )
    user = serializers.StringRelatedField()

    class Meta:
        model = Comments
        fields = "__all__"