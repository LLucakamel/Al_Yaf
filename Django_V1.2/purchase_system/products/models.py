from django.db import models
from orders.models import Order  # Import the Order model

class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='products/images/')
    stock = models.IntegerField(default=0)  # Added stock field
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:  # If it's an existing instance
            old_product = Product.objects.get(pk=self.pk)
            if old_product.quantity != self.quantity:  # Check if quantity has changed
                self.stock = self.quantity  # Update stock to match new quantity
        else:
            self.stock = self.quantity  # Initialize stock with quantity for new products
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name