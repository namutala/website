from django.contrib import admin
from .models import  Item, Order, OrderItem, Item_details

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Item_details)
