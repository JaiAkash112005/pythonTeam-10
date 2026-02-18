from django.urls import path
from .views import booking_api

urlpatterns = [
    path('', booking_api),
    path('<int:booking_id>/', booking_api),
]
