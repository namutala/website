from django.urls import path
from . import views


urlpatterns = [
    path('', views.service_request, name='services'),
    path('booking/', views.book_service, name= 'service-booking'), 
]

