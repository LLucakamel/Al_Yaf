from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Order, Product
from django.db.models import Q

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['requester']  # Exclude the requester field from the form
        fields = '__all__'
        widgets = {
            'request_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date().isoformat()}),
            'supply_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date().isoformat()}),
            }