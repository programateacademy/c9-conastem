from django.db import models
from django.db.models import F, Q, When
from ..Person_Responsable import PersonResponsable
from ...models.Criterio import Criterio

class Sostenibilidad(models.Model):

    criterio = models.ForeignKey(Criterio, on_delete=models.SET_NULL, null=True)

    ITEM_CHOICE = [
        ("Se cuenta con un plan de financiación estatal o privado que aporte al programa y cubra por lo menos cinco años del proyecto", "1"),
        ("El equipo líder cuenta con condiciones laborales y de infraestructura específicas que garantizan la proyección del programa a través de los años", "2"),
        ("El equipo líder asegura que todas las partes interesadas tengan oportunidades continuas para acceder a la información y aprender sobre la implementación de STEM", "3"),
        ("El Programa en Educación STEM estableció y monitorea los indicadores de gestión que miden el éxito del programa", "4"),
        ("El Programa en Educación STEM tiene establecido un proceso de auditoría interna/externa cada dos años", "5"),
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