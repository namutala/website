from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ="Item-list"),
    path('Item_details/', views.product_details, name ='item-details'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart_view, name='cart-view'),
    path('remove-item/<int:item_id>/', views.remove_item, name='remove-item')
]

