from django.contrib import admin
from .models import workout_group, Workout_sessions, exercise, personal_best

# Register your models here.
admin.site.register(workout_group)
admin.site.register(Workout_sessions)
admin.site.register(exercise)
admin.site.register(personal_best)
