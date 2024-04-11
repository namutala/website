from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ="Item-list"),
    path('Item_details/', views.product_details, name ='item-details'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart_view, name='cart-view'),
<<<<<<< HEAD
    path('remove-item/<int:item_id>/', views.remove_item, name='remove-item')
=======
    path('remove-item/<int:item_id>/', views.remove_item, name='remove-item'),
    path('create_order/', views.create_order, name='create-order'),
    path('order_details/<int:order_id/', views.order_detail, name = 'order-details'),
    
>>>>>>> 43d7502b476db0558d04235a364da895b44c6b79
]

