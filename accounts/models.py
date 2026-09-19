from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=11)
    
    def __str__(self):
        return self.first_name + " - " + self.last_name