from .models import Order, OrderItem
from django import forms
from django.contrib.auth.models import User

class  OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['']
        