from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Simulation
from .serializers import SimulationSerializer
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

class SimulationView(APIView):
    def post(self, request):
        # Parse input data
        doctor = request.data.get('doctor')
        patient = request.data.get('patient')
        param1 = float(request.data.get('parameter1'))
        param2 = float(request.data.get('parameter2'))

        # Perform simulation: Example linear model y = param1 * x + param2
        x = np.linspace(0, 10, 100)
        y = param1 * x + param2

        # Save results in database
        simulation = Simulation.objects.create(
            doctor=doctor,
            patient=patient,
            parameter1=param1,
            parameter2=param2,
            result={'x': x.tolist(), 'y': y.tolist()},
        )
        simulation.save()

        # Generate plot
        plt.figure()
        plt.plot(x, y, label=f"y = {param1}x + {param2}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Simulation Result")
        plt.legend()

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()

        return Response({
            "simulation_id": simulation.id,
            "plot": image_base64,
            "result": simulation.result,
        }, status=status.HTTP_201_CREATED)
