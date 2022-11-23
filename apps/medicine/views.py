from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404
from rest_framework import generics

from .models import Medication, Vaccine
from .serializers import MedicationSerializer, VaccineSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class MedicationCreateList(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer
   # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)

class UserPartMedicationList(generics.ListAPIView):
    serializer_class = MedicationSerializer
   # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Medication.objects.filter()



class MedicationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Medication.objects.filter(user=self.request.user)


class VaccineCreateList(generics.ListCreateAPIView):
    serializer_class = VaccineSerializer
    queryset = Vaccine.objects.filter()
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Vaccine.objects.filter(user=self.request.user)


class UserPartVaccineList(generics.ListAPIView):
    serializer_class = VaccineSerializer
    queryset = Vaccine.objects.filter()
    #permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Vaccine.objects.filter()


class VaccineRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VaccineSerializer
    queryset = Vaccine.objects.filter()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Vaccine.objects.filter(user=self.request.user)
