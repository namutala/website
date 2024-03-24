from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth import get_user
from PIL import Image


class Customer(models.Model):
    name = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    city = models.CharField(max_length=200,null=True,blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return f'{self.name.username} details' 
    
    
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
CATEGORY_CHOICES = (
    ('food and beverages','food and beverages'),
    ('phones','phones'),
    ('outdoor','outdoor'),
    ('indoor','indoor'),
    ('watches and jewelry','watches and jewelry'),
    ('books and stationery','books and stationery'),
    ('toys','toys'),
    ('games','games'),
    ('shoes','shoes'),
    ('bags', "bags"),
    ('electronics','electronics'),
    ('health and beauty', 'health and beauty'),
    ('sports','sports'),
    ('furniture','furniture'),
    ('music','music'),
    ('baby','baby'),
    ('fitness and gym','fitness and gym'),
    ('kitchen and dining','kitchen and dining')
    )
LABEL_CHOICES = (
    ('new','new'),
    ('flash sale', 'flash sale'),
    ('limited','limited')
)
class Item(models.Model):
    title = models.CharField(max_length =100)
    picture = models.ImageField(default='default.jpg', upload_to = 'item_pics')
    price  = models.FloatField()
    category = models.CharField(choices =CATEGORY_CHOICES, max_length =30, default =None)
    label = models.CharField(choices = LABEL_CHOICES, max_length = 15, default =None)
    
    def __str__(self):
        return self.title
    
class Item_details(models.Model):
    item = models.OneToOneField(Item, on_delete = models.CASCADE, related_name ='details')
    description = models.TextField(max_length =500)
    key_features = models.TextField(max_length= 200) 

    def __str__(self):
        return f'{self.item.title} description'
       
    
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
    
    

