from django.db import models

from customers.models import Customer
from products.models import Product

# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateField()

    def __str__(self):
        return f"{self.customer} - {self.product}({self.quantity})"