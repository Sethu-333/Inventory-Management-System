from django.db import models

class products(models.Model):

    product_name = models.CharField(max_length= 100, null= True)
    product_code = models.CharField(max_length= 100, null= True)
    price = models.FloatField(default= 0)
    gst = models.FloatField( default= 0)
    food_product = models.BooleanField(default= False)
    picture = models.ImageField(blank=True, null= True, upload_to='images/products/')

    def __str__(self):
        return self.product_name 