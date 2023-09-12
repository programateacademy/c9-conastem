from django.db import models
from django.db.models import F, Q, When
from ..Person_Responsable import PersonResponsable
from ...models.Criterio import Criterio

class DesarrolloDeEquiposLideres(models.Model):
    
    criterio = models.ForeignKey(Criterio, on_delete=models.SET_NULL, null=True)

    ITEM_CHOICE = [
        ("El equipo de liderazgo de educación STEM está definido y nombrado en la institución para establecer monitorear y evaluar el programa completo.", "1"),
        ("Los equipos de docentes abordan las expectativas específicas del programa establecido por el equipo líder.", "2"),
        ("El equipo líder se reúne regularmente para discutir investigaciones, mejores prácticas, éxitos y oportunidades de mejora hacia los objetivos del Programa en Educación STEM.", "3"),
        ("La toma de decisiones es realizada por todo el personal de la institución, el aula y los docentes de áreas especiales.", "4"),
        ("El equipo líder establece un proceso de evaluación del Programa en Educación STEM de forma anual para medir los avances en los diferentes aspectos que componen esta transformación.", "5"),
        
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