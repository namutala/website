from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class service(models.Model):
    service_name = models.CharField(max_length = 100)
    service_description = models.TextField(max_length =800)
    service_price = models.IntegerField()
   
class booking(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    service_booked = models.ForeignKey(service , on_delete = models.CASCADE)
    date_booked = models.DateTimeField(default = timezone.now)
    start_time= models.DateTimeField()

    def __str__(self):
        return f'Booking for {self.customer} by {self.customer} '
    