from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Order, Item, OrderItem, Item_details
from django.template.loader import get_template
from django.urls import reverse

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

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart
    return redirect('cart-view')

def cart_view(request):
    cart = request.session.get('cart', {})
    item_ids = cart.keys()
    items = Item.objects.filter(id__in=item_ids)
    cart_items = [(item, cart[str(item.id)]) for item in items]
    total_price = sum(item.price * quantity for item, quantity in cart_items)
    return render(request, 'storefront/cart.html', {'cart_items': cart_items, 'total_price': total_price})


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
