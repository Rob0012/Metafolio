
from django.db import models


class User(models.Model):
    user = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/')
    email = models.EmailField() 
    phone_number = models.CharField(max_length=15)
    password = models.CharField(max_length=255)