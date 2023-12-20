from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import MFRESerializer
from .models import MFRE_model

# Create your views here.

class MFREView(viewsets.ModelViewSet):
    serializer_class = MFRESerializer
    queryset = MFRE_model.objects.all()

    def retrieve(self, request, *args, **kwargs):
        modelInstance = self.get_object()
        calculated_data = self.perform_calculations(modelInstance)
        serializer = self.get_serializer(calculated_data)
        return Response(serializer.data)

    def perform_calculations(self, modelInstance):
        modelInstance.parkingSpotsPerUnit = modelInstance.numParkingSpots / modelInstance.numApartmentUnits
        return modelInstance
    
    