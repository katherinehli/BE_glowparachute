from django.db import models

# Create your models here.

class Tranche(models.Model):
    placeholderString = "hello"
    loanToValue = models.FloatField(default=0.0)

    def _str_(self):
        return self.placeholderString

    def deconstruct(self):
        return 'django-finModel.MFRE_model.models.Tranche', [], {}

    def __eq__(self, other):
        return self.loanToValue == other.loanToValue

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
    acquisitionPrice = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    exitDate = models.DateField(default='2000-01-01')

    # tranches = models.ForeignKey(tranche, on_delete=models.CASCADE, default=None)
    tranches = models.ForeignKey(Tranche, on_delete=models.CASCADE, null=True, blank=True)

    # Tranches here - ordered list of tranches. create class of tranches

    def __str__(self):
        return self.buildingName

