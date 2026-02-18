from django.urls import path
from .views import resource_api

urlpatterns = [
    path('', resource_api),
]
