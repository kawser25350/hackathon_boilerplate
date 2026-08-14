"""
URL configuration for auth app.
"""

from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('edit/', views.ChangeUserForm.as_view(), name='edit'),
]
