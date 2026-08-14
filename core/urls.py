from django.urls import path
from .views import IdeaDashboardView

urlpatterns = [
    path('', IdeaDashboardView.as_view(), name='home'),
    
]
