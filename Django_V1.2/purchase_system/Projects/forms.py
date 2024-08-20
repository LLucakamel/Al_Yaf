from django import forms
from .models import Project, ProjectPhase

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'code', 'consultant', 'location']
        labels = {
            'name': 'Project Name',
            'code': 'Project Code',
            'consultant': 'Project Consultant',
            'location': 'Project Location'
        }

class ProjectPhaseForm(forms.ModelForm):
    class Meta:
        model = ProjectPhase
        fields = ['code', 'phase_name']

class EditPhaseForm(forms.ModelForm):
    class Meta:
        model = ProjectPhase
        fields = ['code', 'phase_name']