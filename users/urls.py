from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='site-home'),
    path('login/',views.login, name="login"),
]