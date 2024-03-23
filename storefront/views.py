from django.shortcuts import render
from .models import Customer, Order, Item, OrderItem, Item_details

def home(request):
    context ={
        'product' :Item.objects.all()
              }
    return render(request, "storefront/home.html", context)


def product_details(request):
    context ={
        'item_details': Item_details.objects.all()
    }
    return render(request, 'storefront/Item_details.html', context)

def Order_details(request):
    context = {
        'Orders' : Order.objects.all()
    }
    return render(request, 'storefront/Order_details.html', context)

def Item_list(request):
    context = {
        'Item' :Item.objects.all()
    }
    return render(request, 'storefront/Item_list.html', context)
