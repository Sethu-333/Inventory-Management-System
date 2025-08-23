from django.db import models
from Inventory.models import *

# Create your models here.
class customer(models.Model):
    customer_name = models.CharField(max_length= 100, null=False)
    customer_since = models.DateField(null=True)
    customer_pic = models.ImageField(null=True, blank=True, upload_to='images/profile/')

    def __str__(self):
        return self.customer_name

class order(models.Model):
    customer_referance = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)
    product_referance = models.ForeignKey(products, on_delete=models.SET_NULL, null=True)
    order_number = models.CharField(max_length= 100, null=True)
    order_date = models.DateField(null=True)
    quantity = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    gst_amount = models.FloatField(default=0)
    bill_amount = models.FloatField(default=0)

    def __str__(self):
        return self.order_number