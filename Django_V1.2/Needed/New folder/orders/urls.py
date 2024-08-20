from django.urls import path
from . import views
from .views import project_search_view  # Import the missing view

urlpatterns = [
    path('add/', views.add_order, name='add_order'),
    path('', views.order_list, name='order_list'),  # Add this line
    path('project-search/', views.project_search, name='project_search'),
    path('product-search/', views.product_search, name='product_search'),
    path('order/review/<int:order_id>/', views.order_review, name='order_review'),
]