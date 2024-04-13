from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Order, Item, Item_details
from django.template.loader import get_template
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
from django.contrib import messages
from services.models import service


def home(request):
    service_names = service.objects.values_list('service_name', flat=True)
    context ={
        'product' :Item.objects.all(), 'service_names': service_names
              }
    
    return render(request, "storefront/home.html", context)


def product_details(request):
    context ={
        'item_details': Item_details.objects.all()
    }
    return render(request, 'storefront/Item_details.html', context)

def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    quantity = int(request.POST.get('quantity', 1))
    
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + quantity
    request.session['cart'] = cart
    return redirect('cart-view')

def cart_view(request):
    cart = request.session.get('cart', {})
    item_ids = cart.keys()
    items = Item.objects.filter(id__in=item_ids)
    cart_items = [(item, cart[str(item.id)]) for item in items]
    total_items = sum(quantity for _, quantity in cart_items)
    total_price = sum(item.price * quantity for item, quantity in cart_items)
    return render(request, 'storefront/cart.html', {'cart_items': cart_items, 'total_price': total_price, 'total_items' :total_items})

def remove_item(request, item_id):
    cart =request.session.get('cart', {})
    del cart[str(item_id)] # remove item from the cart
    request.session['cart'] = cart
    return redirect('cart-view')



def Order_details(request):
    context = {
        'Orders' : Order.objects.all()
    }
    return render(request, 'storefront/Order_details.html', context)

@login_required
def create_order(request, total_price= None):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = total_price  # Set the total price
            order.save()
            messages.success(request, "An email has been sent to verify the order")
            form.save()
            return redirect('Item-list')
    else:
        form = OrderForm(initial={'total_price': total_price})
    return render(request, 'storefront/create_order.html', {'form': form, 'total_price': total_price})



def Item_list(request):
    context = {
        'Item' :Item.objects.all()
    }
    return render(request, 'storefront/Item_list.html', context)


   