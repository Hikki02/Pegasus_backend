from django.urls import path

from . import views

urlpatterns = [
    path('medication/', views.MedicationCreateList.as_view()),
    path('medication/<int:pk>', views.MedicationRetrieveUpdateDestroy.as_view()),

    path('vaccine/', views.VaccineCreateList.as_view()),
    path('vaccine/<int:pk>', views.VaccineRetrieveUpdateDestroy.as_view()),

]
