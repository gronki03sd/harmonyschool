from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Incident
from .forms import IncidentForm  # We'll create this next
from .filters import IncidentFilter
from django_filters.views import FilterView

from django.views.generic import DetailView

class IncidentListView(LoginRequiredMixin, FilterView):
    model = Incident
    template_name = 'incidents/incident_list.html'
    filterset_class = IncidentFilter
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(created_by=self.request.user)
        return queryset.order_by('-created_at')
    
class IncidentCreateView(LoginRequiredMixin, CreateView):
    model = Incident
    form_class = IncidentForm  # Use this instead of fields
    template_name = 'incidents/incident_create.html'
    success_url = '/incidents/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    


class IncidentDetailView(LoginRequiredMixin, DetailView):
    model = Incident
    template_name = 'incidents/incident_detail.html'
    context_object_name = 'incident'