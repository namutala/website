from django.urls import path
from . import views

urlpatterns = [
    path('',views.Item_list, name ="Item_list")
]

