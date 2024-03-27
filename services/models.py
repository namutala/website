from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class service(models.Model):
    service_name = models.CharField(max_length = 100)
    service_description = models.CharField(default ='service description', max_length=600)
    service_prices = models.CharField(max_length = 100) 
    
    def __str__(self):
        return {self.service_name}
    
class serviceImage(models.Model):
    service = models.ForeignKey(service, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='service_images')
    
    def __str__(self):
        return f'{self.service.service_name} Views'

    def __str__(self):
        return f"Image for {self.service.service_description}"
    
class booking(models.Model):
    customer = models.ForeignKey(User, on_delete = models.CASCADE)
    service_booked = models.ForeignKey(service, on_delete = models.CASCADE)
    date_booked = models.DateTimeField(default =timezone.now)
    start_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Booking of {self.service_booked} by {self.customer}'
    
