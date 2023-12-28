from rest_framework import serializers
from .models import MFRE_model

class MFRESerializer(serializers.ModelSerializer):
    class Meta:
        model = MFRE_model
        fields = ('id', 'buildingName', 'dealName', 'locationDescription', 'numApartmentUnits', 'numParkingSpots', 'parkingSpotsPerUnit', 'tranche')