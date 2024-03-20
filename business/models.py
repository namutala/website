from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Business(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    business_name = models.CharField(max_length=35, default ='Business name')
    logo = models.ImageField(default='default.jpg', upload_to='business_logos')
    business_description = models.TextField(max_length=200)
    location = models.TextField(max_length = 50)
    email = models.EmailField()
    contact = models.IntegerField()

    def _str_(self):
        return f'{self.owner.username} Business'

class BusinessImage(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='catalogue_images')
    image = models.ImageField(upload_to='business_catalogue')

    def _str_(self):
        return f'Image for {self.business.business_name}'

