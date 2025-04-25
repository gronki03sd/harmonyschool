from django import forms
from .models import Incident, Category, Location

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'status', 'description', 'category', 'priority', 'location']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'priority': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Set querysets
        self.fields['category'].queryset = Category.objects.all()
        self.fields['location'].queryset = Location.objects.all()
        
        # Add Bootstrap classes to all fields
        for field_name, field in self.fields.items():
            if 'class' not in field.widget.attrs:
                field.widget.attrs['class'] = 'form-control'
                
        # Customize choice fields
        self.fields['status'].choices = Incident.STATUS_CHOICES
        self.fields['priority'].choices = Incident.PRIORITY_CHOICES
        
        # Add placeholders
        self.fields['title'].widget.attrs['placeholder'] = 'Enter incident title'
        self.fields['description'].widget.attrs['placeholder'] = 'Describe the incident in detail'