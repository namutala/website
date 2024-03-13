from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to = 'profille_pics')
    Bio= models.TextField(default = 'Hello I use localbiconnect')
    

    def __str__(self):
        return f'{self.user.username} Profile'
    
