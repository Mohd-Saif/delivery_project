# tracking/urls.py

from django.urls import path
from .views import LocationUpdateView

urlpatterns = [
    path('api/update-location/', LocationUpdateView.as_view(), name='update-location'),
]
