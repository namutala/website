from django.urls import path
from . import views

urlpatterns = [
    path('', views.register_business, name='register_biz'),
    path('catalogue/', views.add_catalagoue, name = 'register_cart')
]