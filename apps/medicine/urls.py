from django.urls import path
from rest_framework import routers

from apps.medicine import views

from .models import Medication
from . import views

urlpatterns = [
    path('medicine/', views.MedicationCreateList.as_view()),
    path('medicine/<int:pk>', views.MedicationRetrieveUpdateDestroy.as_view()),

    path('vaccine/', views.VaccineCreateList.as_view()),
    path('vaccine/<int:pk>', views.VaccineRetrieveUpdateDestroy.as_view()),

]
