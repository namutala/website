from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user


class Customer(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.name.username} details' 
    
class Product(models.Model):
    CATEGORY = (
        ('Indoor', 'Indoor'),
        ('Outdoor', 'Outdoor'),
        )
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True, choices=CATEGORY)
    description = models.TextField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.name}'
    
#class Ordered(models.Model):
 #   STATUS = (
  #      ('Pending', 'Pending'),
   #     ('Out of delivery', 'Out of delivery'),
    #    ('Delivered', 'Delivered'),
     #        )
    #customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    #product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    #date_created = models.DateTimeField(auto_now_add=True, null=True)
    #status = models.CharField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return f'{self.customer} order' 
# refresh
class Item(models.Model):
    title = models.CharField(max_length =100)
    price  = models.FloatField()
    
    def __str__(self):
        return self.title
    
class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete =models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(default=timezone.now, editable=False)
    ordered_date = models.DateTimeField(default=timezone.now, editable=False)
    ordered = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        current_user = get_user()
        if isinstance(current_user, AnonymousUser):
            # If the user is not logged in, handle it accordingly
            # For example, you can set user to None or any default user
            self.user = None
        else:
            self.user = current_user
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Order #{self.pk} by {self.user.username}'
    
    

