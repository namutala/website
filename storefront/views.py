from django.shortcuts import render
from .models import Customer, Product, Order, Item, OrderItem

def home(request):
    context ={
        'product' :Item.objects.all()
              }
    return render(request, "storefront/home.html", context)

def Product_details(request):
    context ={
        'products': Product.objects.all()
    }
    return render(request, 'storefront/Product_details.html', context)

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
def products(request):
    context ={
        'product' :Product.objects.all()
              }
    return render(request, "storefront/products.html", context)
