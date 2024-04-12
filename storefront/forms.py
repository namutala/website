from .models import Order
from django import forms
from django.contrib.auth.models import User

class  OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['user','item','order_status']
        widgets = {
            'total_price': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make the total price field read-only
        }
        
          