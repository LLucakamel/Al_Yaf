from django.urls import path
from . import views
from .views import project_search_view, update_order  # Removed review_order from the import

urlpatterns = [
    path('add/', views.add_order, name='add_order'),
    path('', views.order_list, name='order_list'),  # Add this line
    path('project-search/', views.project_search, name='project_search'),
    path('product-search/', views.product_search, name='product_search'),
    path('api/phases/', views.project_phase_list_api, name='api_phases'),
    path('approve-order/<int:order_id>/', views.approve_order, name='approve_order'), # Added new URL for approve order
    path('edit-order/<int:order_id>/', views.edit_order, name='edit_order'), # Updated URL for edit order
    path('reject-order/<int:order_id>/', views.reject_order, name='reject_order'),
]