from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=32)
    lname = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    email = models.EmailField()
    message = models.TextField()