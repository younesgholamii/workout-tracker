from django.db import models
from ..utils import category_choices, status_choices

class Plans(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=category_choices, default='cardio')
    status = models.CharField(max_length=50, choices=status_choices, default='pending')
    date = models.DateTimeField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def day_of_week(self):
        return self.date.strftime('%A')
    
    def time(self):
        return self.date.strftime('%H:%M')
    
