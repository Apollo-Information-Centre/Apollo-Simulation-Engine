from django.db import models
import datetime

class Simulation(models.Model):
    doctor = models.CharField(max_length=255, default="Unknown Doctor")
    patient = models.CharField(max_length=255, default="Unknown Patient")
    parameter1 = models.FloatField(default=0.0)
    parameter2 = models.FloatField(default=0.0)
    result = models.JSONField(default=dict)  # Store result as a dictionary
    created_at = models.DateTimeField(default=datetime.datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Simulation between {self.doctor} and {self.patient}"
