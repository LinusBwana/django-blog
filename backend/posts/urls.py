from django.urls import include, path
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls)),
]