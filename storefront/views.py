from django.shortcuts import render
from .models import Customer, Product, Order

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


