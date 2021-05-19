from django.db import models
from django import forms
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    brand=models.CharField(max_length=100)
    prce=models.FloatField()
    contInstock=models.IntegerField()
    image=models.ImageField(upload_to="images/")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name