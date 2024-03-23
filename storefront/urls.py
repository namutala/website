from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ="Item-list"),
    path('Item_details/', views.product_details, name ='item-details')
]

