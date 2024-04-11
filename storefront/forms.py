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
        
        
'''  user  = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null = True)
    total_price = models.DecimalField(max_digits=20, decimal_places=1, default = 0)
    location = models.CharField(max_length= 40, null= False, default= 'enter delivery location')
    order_status = models.CharField(max_length=20, choices= STATUS, default = 'Pending')
    created_at = models.DateTimeField(default= timezone.now)
    payment_method = models.CharField(choices= PAYMENT, default = 'Cash On Delivery')
   '''     