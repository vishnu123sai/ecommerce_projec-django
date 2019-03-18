from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length = 400)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    img_link = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    first_name = models.CharField(max_length = 400)
    last_name = models.CharField(max_length = 400)
    email = models.CharField(default=None, max_length = 400)
    address = models.TextField()
    city  = models.CharField(max_length = 400)
    mobile_no = models.IntegerField(default=None)
    pin_code = models.IntegerField(default=None)
    payment_date = models.CharField(max_length = 400)
    items = models.TextField()

    def __str__(self):
        return self.email

    


