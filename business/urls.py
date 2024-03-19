from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_business, name='register_biz'),
    path('profile/', views.business_profile, name='biz_profile')
]