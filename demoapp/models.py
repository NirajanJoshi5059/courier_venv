from pyexpat import model
from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=255, unique=True)
    price=models.CharField(max_length=255)
    category=models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

 