
from django.db import models

# Create your models here.
class Item(models.Model):
    item=models.CharField(max_length=100)
    categories_choices = (('APPETIZERS','APPETIZERS'),('VEGETARIAN DOSAS','VEGETARIAN DOSAS'),('NON-VEGETARIAN DOSAS','NON-VEGETARIAN DOSAS'),
                          ('VEGETARIAN SPECIALTIES','VEGETARIAN SPECIALTIES'),('NON-VEGETARIAN SPECIALTIES','NON-VEGETARIAN SPECIALTIES'),
                          ('SEA FOOD ENTREES','SEA FOOD ENTREES'),('DESSERTS & BEVERAGES','DESSERTS & BEVERAGES'))
    item_description=models.TextField(default='')
    category=models.TextField(choices=categories_choices)

class Contact(models.Model):
    name=models.CharField(max_length=100,verbose_name="")
    email=models.EmailField(verbose_name="")
    phone=models.CharField(default="",max_length=10,verbose_name="")
    message=models.TextField(default="",verbose_name="")
