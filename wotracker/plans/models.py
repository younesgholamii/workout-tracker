from django.db import models


class PlansModel(models.Model):
    category_choices = [
        ('cardio', 'Cardio'),
        ('strength', 'Strength'),
        ('flexibility', 'Flexibility')
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50 ,choices=category_choices, default='cardio')
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
