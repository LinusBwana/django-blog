from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comments(models.Model):
    comment_content = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.comment_content
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'