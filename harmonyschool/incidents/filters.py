import django_filters
from .models import Incident, Category, Location
from django import forms

class IncidentFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search by title'})
    )
    status = django_filters.ChoiceFilter(
        choices=Incident.STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    priority = django_filters.ChoiceFilter(
        choices=Incident.PRIORITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    location = django_filters.ModelChoiceFilter(
        queryset=Location.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Incident
        fields = ['title', 'status', 'priority', 'category', 'location']