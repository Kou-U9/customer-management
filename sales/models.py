from django.db import models
from django.utils.timezone import now
import uuid

# Create your models here.
class Sale(models.Model):
    sale_number = models.CharField(max_length=12, unique=True, editable=False)
    sale_date = models.DateField()
    customer_name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.sale_number:
            self.sale_number = self.generate_sale_number()
        self.total_amount = sum(item.total_price() for item in self.items.all())
        super().save(*args, **kwargs)

    def generate_sale_number(self):
        date_part = now().strftime('%Y%m%d')
        random_part = str(uuid.uuid4().int)[:4]
        return f'{date_part}{random_part}'
    
    def __str__(self):
        return f"Sale {self.sale_number} - {self.customer_name} - Total: {self.total_amount}"
    
class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, related_name='items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def total_price(self):
        return self.quantity * self.price
    
    def __setr__(self):
        return f"{self.product_name} - {self.quantity} ✕ {self.price}"
