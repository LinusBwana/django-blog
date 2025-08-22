from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Posts(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.post_title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.post_title
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"