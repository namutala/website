from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class service(models.Model):
    service_name = models.ForeignKey(User, on_delete = models.CASCADE)
    service_description = models.CharField(default ='service description', max_length=600)
    service_prices = models.CharField(max_length = 100) 
    
class booking(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    service_booked = models.ForeignKey(service, on_delete = models.CASCADE)
    date_booked = models.DateTimeField(default =timezone.now)
    start_date = models.DateTimeField(auto_now_add=True)
    
