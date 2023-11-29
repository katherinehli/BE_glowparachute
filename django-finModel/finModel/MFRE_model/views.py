from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MFRESerializer
from .models import MFRE_model

# Create your views here.

class MFREView(viewsets.ModelViewSet):
    serializer_class = MFRESerializer
    queryset = MFRE_model.objects.all()