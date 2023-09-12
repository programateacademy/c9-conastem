from django.db import models
from django.db.models import F, Q, When
from ..Person_Responsable import PersonResponsable
from ...models.Criterio import Criterio

class Equidad(models.Model):

    criterio = models.ForeignKey(Criterio, on_delete=models.SET_NULL, null=True)

    ITEM_CHOICE = [
        ("Uso de la información de pruebas estandarizadas estatales, además de otras evaluaciones", "1"),
        ("Seguimiento riguroso a la información de las evaluaciones formativas", "2"),
        ("Hay un proyecto de seguimiento del avance del programa con los estudiantes.", "3"),
        ("Existe un plan individual de educación para cada estudiante", "4"),
        ("Se utilizan sistemas de protección y de seguimiento de la información", "5"),
        ("Los estudiantes y los padres tienen acceso a información", "6"),
    ]
    
    numeral = models.CharField (max_length=1000, choices= ITEM_CHOICE)
    
    PRIORITY_MODEL_CHOICE = (
        (" ", "Exploratorio"),
        (" ", "Introductorio"),
        ("", "Inmerción parcial"),
        (" ", "Inmerción completa"),
    )

    priority_model = models.CharField (max_length=4, choices= PRIORITY_MODEL_CHOICE, default= "Introductorio")
    
    dep_responsable = models.CharField (max_length=30, default= "Dirección")
    
    person_responsable = models.ManyToManyField(PersonResponsable, help_text= "Seleccione un responsable")
    
    track_year = models.IntegerField (help_text="Ingrese año de seguimiento")
    
    track_date = models.CharField(max_length=5, help_text="Ingrese fecha de seguimiento")
    
    internal_auditory_date = models.DateField(default="31/01/2000", null= True)
    internal_auditory_obs = models.TextField(max_length=1000, blank= True)

    external_auditory_date = models.DateField(default="31/01/2000", null= True, blank= True)
    external_auditory_obs = models.TextField(max_length=1000, blank= True)

    def __str__(self):
        return self.numeral