"""URL patterns for base app."""
from django.urls import path
from .views import RonehaView

urlpatterns = [
    path('', RonehaView.as_view(), name='roneha'),
]
