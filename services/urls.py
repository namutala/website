from django.urls import path
from . import views


urlpatterns = [
    path('', views.service_request, name='services'),
    path('booking/<int:service_id>/', views.book_service, name='book-service'),
]
