from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class workout_group(models.Model):
    group = models.CharField(max_length=100)

    def __str__(self):
        return self.group
    
class Workout_sessions(models.Model):
    workout_group = models.ForeignKey(workout_group, on_delete=models.CASCADE)
    session_date = models.DateField()
    

    def __str__(self):
        return f"{self.workout_group} - {self.session_date}"


class exercise(models.Model):

    KG = 'kg'
    BARS = 'bars'

    UOM_CHOICES = [
        (KG, 'Kg'),
        (BARS, 'Bars'),
    ]

    workout_group = models.ForeignKey(workout_group, on_delete=models.CASCADE)
    exercise =  models.CharField(max_length=100)
    uom = models.CharField(max_length=10, choices=UOM_CHOICES)
    max_weight = models.FloatField()

    def __str__(self):
        return f"{self.workout_group} {self.exercise} ({self.uom})"