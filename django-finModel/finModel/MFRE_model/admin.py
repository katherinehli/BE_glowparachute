from django.contrib import admin
from .models import MFRE_model

class MFRE_modelAdmin(admin.ModelAdmin):
    list_display = ('id', 'buildingName', 'dealName', 'locationDescription', 'numApartmentUnits', 'numParkingSpots', 'parkingSpotsPerUnit', 'tranche')

# Register your models here.


admin.site.register(MFRE_model, MFRE_modelAdmin)