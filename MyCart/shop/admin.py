from django.contrib import admin
from .models import Order, Product, Contact, OrderUpdate
# Register your models here.

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)