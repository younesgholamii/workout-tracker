from django.contrib import admin
from .models import Exercise, WorkoutExercise, WorkoutPlan


admin.site.register(WorkoutPlan)
admin.site.register(Exercise)
admin.site.register(WorkoutExercise)