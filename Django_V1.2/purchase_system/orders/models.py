from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

class Order(models.Model):
    order_name = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('disapproved', 'Disapproved')
    ], default='pending')
    
    project_name = models.CharField(max_length=255)
    project_code = models.CharField(max_length=100)
    project_phase = models.CharField(max_length=100)
    project_consultant = models.CharField(max_length=255)
    project_location = models.CharField(max_length=255)
    request_date = models.DateField(default=timezone.now)  # Set default to the current date
    supply_date = models.DateField()   # This will be handled in the form to restrict past dates
    products = models.ManyToManyField('products.Product', related_name='product_orders')
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    unit = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"M-{str(self.id).zfill(3)}"  # Custom order number format

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)  # Save the order