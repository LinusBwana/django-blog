from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    follows = models.ManyToManyField("self", related_name="followed_by", symmetrical=False, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


# Creating profile when a new User Signs Up
# @receiver(post_save, sender=User) # Alternative
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(user=instance)
        user_profile.save()
        # follow themselves
        user_profile.follows.add(user_profile)
        user_profile.save()
post_save.connect(create_profile, sender=User)