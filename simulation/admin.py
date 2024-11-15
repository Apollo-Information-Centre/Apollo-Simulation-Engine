from django.contrib import admin
from .models import Simulation

class SimulationAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'patient', 'created_at', 'updated_at')  # Display fields in the list view
    search_fields = ('doctor', 'patient')  # Allow search by doctor or patient
    list_filter = ('created_at',)  # Filter by creation date

# Register the Simulation model with custom options
admin.site.register(Simulation, SimulationAdmin)
