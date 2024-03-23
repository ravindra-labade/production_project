from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=10)
    product_price = models.IntegerField()
    product_quantity = models.IntegerField()
    delivery_address = models.CharField(max_length=20)
    choice = [('Online', 'ONLINE'), ('Cash', 'Cash On Delivery')]
    payment_mode = models.CharField(max_length=10, choices=choice)

