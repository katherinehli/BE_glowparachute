from django.db import models

# Create your models here.

class MFRE_model(models.Model):
    buildingName = models.CharField(max_length=300, default='Building Name N/A')
    dealName = models.CharField(max_length=120, default='Building Name N/A')
    # locationDescription = models.TextField(max_length=500)
    locationDescription = models.BooleanField(default=False)
    numApartmentUnits = models.IntegerField(default=0)
    parkingSpotsPerUnit = models.IntegerField(default=0)
    rentableToGrossSqFtRatio = models.IntegerField(default=0)
    acquisitionDate = models.DateField(default='2000-01-01')
    goingInCapRate = models.FloatField(default=0.0) # Store percentage values as decimals in the range of 0.0 to 1.0, where 1.0 represents 100%. For example, 0.5 would represent 50%.
    acquistionPrice = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    exitDate = models.DateField(default='2000-01-01')

    # Tranches here - ordered list of tranches. create class of tranches


    def _str_(self):
        return self.title