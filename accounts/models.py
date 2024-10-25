from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class CustomUser(AbstractUser):
    
    class Meta:
        permissions = [
            ('special_status', 'User can access all courses')
        ]
    def get_absolute_url(self):
        return reverse("home")
    
