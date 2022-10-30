from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Medication, Vaccine
from .serializers import MedicationSerializer, VaccineSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class MedicationCreateList(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer
    queryset = Medication.objects.filter()


class MedicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationSerializer
    queryset = Medication.objects.filter()


class VaccineCreateList(generics.ListCreateAPIView):
    serializer_class = VaccineSerializer
    queryset = Vaccine.objects.filter()


class VaccineRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VaccineSerializer
    queryset = Vaccine.objects.filter()

