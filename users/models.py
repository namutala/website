from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profille_pics')
    Bio= models.TextField(default = 'Hello I use localbiconnect')

    def __str__(self):
        return f'{self.user.username} Profile'

class Photo(models.Model):
    image = models.ImageField(upload_to = 'photos/')
class Logo(models.Model):
    image = models.ImageField(upload_to='photos/logos/')
class Business(models.Model):
    name = models.CharField(max_length=100, unique=True)
    contactDetails = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    logo = models.OneToOneField(Logo, on_delete = models.SET_NULL)
    photos = models.ManyToManyField(Photo, related_name='businesses', blank=True)
    menu = models.ForeignKey('Menu', on_delete = models.CASCADE)
    pricing = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.name}'

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)
    items = models.ManyToManyField('MenuItem', related_name='menus')
    def __str__(self):
        return f'{self.name}'
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    def __str__(self):
        return f'{self.name}'