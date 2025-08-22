from django.db import models
from django.contrib.auth.models import User
from posts.models import Posts

# Create your models here.
class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    your_comment = models.TextField()
    commented_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.your_comment
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'