from django.shortcuts import render, redirect, get_object_or_404
from .models import Order
from products.models import Product
from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
import datetime
from django.utils import timezone
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from Projects.models import Project, ProjectPhase  # Import ProjectPhase along with Project
from django.urls import reverse

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product_name', 'product_code', 'quantity', 'project_name', 'project_code', 'order_name', 'project_phase', 'project_consultant', 'project_location', 'request_date', 'supply_date']
        widgets = {
            'request_date': forms.DateInput(attrs={'type': 'date'}),
            'supply_date': forms.DateInput(attrs={'type': 'date', 'min': timezone.now().date().isoformat()}),
        }

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        today = timezone.now().date().isoformat()
        self.fields['request_date'].widget.attrs['min'] = today
        self.fields['supply_date'].widget.attrs['min'] = today
        # Set the request_date field to readonly
        self.fields['request_date'].widget.attrs['readonly'] = True
        if not self.instance.pk:  # Checking if the instance is not saved (i.e., it's new)
            self.fields['request_date'].initial = timezone.now().date()

def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            # هنا يتم إنشاء الطلب والمنتجات بناءً على البيانات المرسلة
            products_data = request.POST.getlist('product_name')
            for name in products_data:
                Product.objects.create(order=order, name=name)
            return redirect('order_list')
    else:
        form = OrderForm()

    return render(request, 'orders/add_order.html', {'form': form})

def order_list(request):
    orders = Order.objects.all()  # Now Order is defined
    return render(request, 'orders/order_list.html', {'orders': orders})

def project_search_view(request):
    # منطق البحث عن المشروع
    data = {}  # تعريف المتغ data كقاموس فارغ
    # يمكنك إضافة بيانات إلى القاموس هنا بناءً على منطق البحث
    return JsonResponse(data)

def product_search(request):
    term = request.GET.get('term', '')
    field = request.GET.get('field', 'name')
    if field == 'name':
        products = Product.objects.filter(name__icontains=term)[:10]
    else:
        products = Product.objects.filter(code__icontains=term)[:10]
    results = [{'label': f"{p.name} ({p.code})", 'value': p.id, 'name': p.name, 'code': p.code} for p in products]
    return JsonResponse(results, safe=False)

def project_search(request):
    term = request.GET.get('term', '')
    projects = Project.objects.filter(name__icontains=term)
    project_list = [
        {
            'name': project.name,
            'code': project.code,
            'id': project.id,
            'consultant': project.consultant if project.consultant else 'No consultant',
            'location': project.location if project.location else 'No location',
        }
        for project in projects
    ]
    return JsonResponse(project_list, safe=False)

from django.http import JsonResponse

def project_phase_list_api(request):
    phases = ProjectPhase.objects.all().values('id', 'phase_name')
    return JsonResponse(list(phases), safe=False)

def approve_order(request):
    # هنا يمكنك إضافة منطق الموافقة على الطلب
    # على سبيل المثال، تغيير حالة الطلب إلى 'موافق عليه'
    return redirect('order_list')  # إعادة التوجيه إلى قائمة الطلبات بعد الموافقة

def edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/edit_order.html', {'form': form})

def reject_order(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.status = 'rejected'  # تحديث حالة الطلب إلى 'مرفوض'
    order.save()
    return redirect('order_list')  # إعادة التوجيه إلى قائمة الطلبات

def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        # Process your form data here
        # For example, update fields in the order object
        order.save()
        return redirect('some_success_url')  # Redirect to a new URL after processing
    return render(request, 'orders/update_order.html', {'order': order})