from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.posts_home, name='home'),
    path('new-post/', views.new_post, name='new_post'),
    path('<slug:slug>/', views.post_details, name='post_details'),
]