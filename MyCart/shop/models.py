from django.db import models
import datetime

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=200, default='')
    subcategory = models.CharField(max_length=200, default='')
    desc = models.CharField(max_length=300, default='')
    price = models.IntegerField(default='')
    pub_date = models.DateField(default='')
    image = models.ImageField(upload_to='shop/images')

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default='')
    phone = models.CharField(max_length=50, default='')
    desc = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.name


class Order(models.Model):

    order_id = models.AutoField(primary_key=True)
    item_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name   


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
    