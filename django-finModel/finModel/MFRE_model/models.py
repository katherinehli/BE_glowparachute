from django.db import models

# Create your models here.

class MFRE_model(models.Model):
    buildingName = models.CharField(max_length=300, default='Building Name N/A')
    dealName = models.CharField(max_length=120, default='Building Name N/A')
    # locationDescription = models.TextField(max_length=500)
    locationDescription = models.BooleanField(default=False)

    def _str_(self):
        return self.title