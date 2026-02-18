from django.urls import path
from .views import create_booking, list_bookings

urlpatterns = [
    path('create/', create_booking),
    path('list/', list_bookings),
]
