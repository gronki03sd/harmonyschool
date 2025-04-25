from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    building = models.CharField(max_length=50, blank=True)
    floor = models.CharField(max_length=20, blank=True)
    room = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.name} ({self.building})"

class Incident(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='medium')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_by = models.ForeignKey(User, related_name='created_incidents', on_delete=models.PROTECT)
    assigned_to = models.ForeignKey(User, related_name='assigned_incidents', null=True, blank=True, on_delete=models.SET_NULL)
    location = models.ForeignKey(Location, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

class Attachment(models.Model):
    file = models.FileField(upload_to='attachments/')
    incident = models.ForeignKey(Incident, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
    
@property
def status_color(self):
    colors = {
        'new': 'secondary',
        'in_progress': 'primary',
        'resolved': 'success',
        'closed': 'dark'
    }
    return colors.get(self.status, 'secondary')