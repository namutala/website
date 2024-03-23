from django.db import models
from business.models import Business
from users.models import User

class Booking(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='bookings')
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'Booking for {self.customer}'