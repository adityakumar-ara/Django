# Create your models here.
# When Ever we use any image in my model we need to run pip install pillow in the terminal


#Whenever we create a model in models.py we need to run two commands in the terminal
#1. python manage.py makemigrations

#2. python manage.py migrate

from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_description = models.TextField()
    product_image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product_name
