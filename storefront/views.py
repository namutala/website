from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer, Order, Item, OrderItem, Item_details
from django.template.loader import get_template
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

@login_required
def create_order(request):
    if request.method == 'POST':
    #retrieving cart items
        cart = request.session.get('cart', {})
    #create new order 
        order = Order.objects.create(user = request.user, total_price =0, location = 'your location')
    
    #calculate total price and create order items
        total_price = 0
        for item_id, quantity in cart.items():
            item = get_object_or_404(Item, id = item_id)
            price = item.price
            total_price += price *quantity
            OrderItem.objects.create(order= order, item = item, quantity = quantity, price= price )
        
    #update total price in the order
        order.total_price = total_price
        order.save()
    
    #clear the cart 
        request.session['cart'] = {}
        return redirect('oder-details', order_id =order.id)

    return render(request, 'storefront/create_order.html')

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id = order_id, user = request.user)
    return render(request, 'storefront/order_detail.html',{'order': order})



    
    

def Item_list(request):
    context = {
        'Item' :Item.objects.all()
    }
    return render(request, 'storefront/Item_list.html', context)
