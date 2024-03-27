from django.urls import path
from . import views


urlpatterns = [
    path('', views.service_request, name='services'),
    path('bookings/', views.booking_request, name= 'booking-request'),
]
