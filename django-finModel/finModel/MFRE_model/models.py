from django.db import models

# Create your models here.

class Tranche(models.Field):
    placeholderString = "hello"
    # loanToValue = models.FloatField(default=0.0)

    def db_type(self, connection):
        return "tranche"

    def __init__(self, loanToValue=0.0, *args, **kwargs):
        self.loanToValue = loanToValue
        super().__init__(*args, **kwargs)

    def _str_(self):
        return self.placeholderString

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["loanToValue"] = self.loanToValue
        return name, path, args, kwargs

    def __eq__(self, other):
        return self.loanToValue == other.loanToValue

class MFRE_model(models.Model):

    # hardcoded fields
    buildingName = models.CharField(max_length=300, default='Building Name N/A')
    dealName = models.CharField(max_length=120, default='Building Name N/A')
    locationDescription = models.TextField(max_length=500, default='N/A')
    numParkingSpots = models.IntegerField(default=0)
    numApartmentUnits = models.IntegerField(default=0)
    rentableToGrossSqFtRatio = models.IntegerField(default=0)
    acquisitionDate = models.DateField(default='2000-01-01')
    goingInCapRate = models.FloatField(default=0.0) # Store percentage values as decimals in the range of 0.0 to 1.0, where 1.0 represents 100%. For example, 0.5 would represent 50%.
    acquisitionPrice = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    exitDate = models.DateField(default='2000-01-01')

    # calculated fields
    parkingSpotsPerUnit = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    # tranches = models.ForeignKey(tranche, on_delete=models.CASCADE, default=None)
    # tranches = models.ForeignKey(Tranche, on_delete=models.CASCADE, null=True, blank=True)

    # Tranches here - ordered list of tranches. create class of tranches
    tranche = Tranche(loanToValue=0.0, null=True, blank=True)

    def __str__(self):
        return self.buildingName

