from django.urls import path
from . import views

urlpatterns = [
    path('', views.IncidentListView.as_view(), name='incident_list'),
    path('create/', views.IncidentCreateView.as_view(), name='incident_create'),
    path('<int:pk>/', views.IncidentDetailView.as_view(), name='incident_detail'),
]