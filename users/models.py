from django.db import models
from app.models import CustomUser

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username
