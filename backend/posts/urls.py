from django.urls import include, path
from .import views

urlpatterns = [
    path('', views.posts_home, name='home'),
    # path('', views.PostsListView.as_view(), name='home'),
    path('new-post/', views.new_post, name='new_post'),
    path('<slug:slug>/', views.post_details, name='post_details'),
    path('post/<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('post/<slug:slug>/edit/', views.edit_post, name='edit_post'),
]