from django.db import models

# Create your models here.
class Product(models.Model):
    fish_name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)
    date = models.DateField(max_length=255)
   
    
    def _str_(self):
        return self.quantity 
        