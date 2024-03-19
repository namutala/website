from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=25, default ='Business name')
    logo = models.ImageField(default='default.jpg', upload_to='business_logos')
    business_description = models.TextField(max_length=150)
    location = models.TextField()
    email = models.EmailField()
    contact = models.IntegerField()

    def _str_(self):
        return f'{self.user.username} Business'

class BusinessImage(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='catalogue_images')
    image = models.ImageField(upload_to='business_catalogue')

    def _str_(self):
        return f'Image for {self.business.business_name}'

