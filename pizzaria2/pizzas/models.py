"""
Author: Brandon Rose
Date: 03-09-18
Class: ICT 4370
Assignment#: 9
Description: Django data model and DB mappings
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping = models.CharField(max_length=30)
    def __str__(self):
        return self.topping

class Post(models.Model):
    selection = models.CharField(max_length=30, default='test')
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.selection

class PizzaSize(models.Model):
    sizes = models.IntegerField(max_length=10)
    def __str__(self):
        return self.sizes

class CrustType(models.Model):
    crust = models.IntegerField(max_length=15)
    def __str__(self):
        return self.crust