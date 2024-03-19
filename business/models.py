from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Business_name = models.TextField(max_length = 25)
    logo = models.ImageField(default='default.jpg', upload_to = 'business_logos')
    Business_description = models.TextField(max_length= 150)
    location = models.TextField()
    email =models.EmailField()
    Conctact = models.IntegerField()
    Cartalogue = models.ImageField()
    
    def __str(self):
        return f'{self.user.username} Business'
    

