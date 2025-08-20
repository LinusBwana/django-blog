from django.shortcuts import render
from rest_framework import viewsets
from .models import UserProfile
from .serializers import UserProfileSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer