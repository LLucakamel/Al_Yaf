from django.urls import path
from .views import project_list, add_project, product_details, edit_project, import_projects, export_projects, search_projects, add_project_phase, ProjectPhaseListView, project_phase_list_api, edit_phase, remove_phase

app_name = 'Projects'

urlpatterns = [
    path('list/', project_list, name='project-list'),
    path('add/', add_project, name='add-project'),
    path('details/<int:project_id>/', product_details, name='product-details'),
    path('edit-project/<int:project_id>/', edit_project, name='edit-project'),
    path('projects/import/', import_projects, name='import-projects'),
    path('projects/export/', export_projects, name='export-projects'),
    path('search/', search_projects, name='search-projects'),
    path('add-phase/', add_project_phase, name='add_phases'),
    path('phases/', ProjectPhaseListView.as_view(), name='project_phase_list'),
    path('api/phases/', project_phase_list_api, name='api_phases'),
    path('phases/edit/<int:id>/', edit_phase, name='edit_phase'),
    path('phases/remove/<int:phase_id>/', remove_phase, name='remove_phase'),
]