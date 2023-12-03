from django.contrib import admin
from .models import MFRE_model

class MFRE_modelAdmin(admin.ModelAdmin):
    list_display = ('buildingName', 'dealName', 'locationDescription')

# Register your models here.

admin.site.register(MFRE_model, MFRE_modelAdmin)