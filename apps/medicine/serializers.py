from rest_framework import serializers

from .models import Medication, Vaccine


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ('id', 'horse', 'title', 'data', 'status')


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = ('id', 'horse', 'title', 'data', 'status')
