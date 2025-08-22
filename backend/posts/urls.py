from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.posts_home, name='home'),
    path('<int:pk>/', views.post_details, name='post_details'),
]