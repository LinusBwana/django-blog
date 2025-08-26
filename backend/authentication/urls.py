from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('forgot-password/', views.forgotPassword, name='forgot-password'),
    path('password-reset-sent/<str:reset_id>/', views.passwordResetSent, name='password-reset-sent'),
    path('reset-password/<str:reset_id>/', views.resetPassword, name='reset-password'),
]