from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Order, Product
from django.db.models import Q

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'product_code', 'quantity', 'unit', 'remarks', 'project_name', 'project_code', 'order_name', 'project_phase', 'project_consultant', 'project_location', 'request_date', 'supply_date']
        widgets = {
            'request_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date().isoformat()}),
            'supply_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date().isoformat()}),
            }
    
class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']