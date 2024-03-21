from django.urls import path
from . import views

urlpatterns = [
    path('',views.Product_details, name ="product-info"),
    path('order_details/', views.Order_details, name= "order-info")
    
]

