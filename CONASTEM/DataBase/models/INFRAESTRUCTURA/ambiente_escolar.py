from django.db import models
from django.db.models import F, Q, When
from ..Person_Responsable import PersonResponsable
from ...models.Criterio import Criterio

class AmbienteEscolar(models.Model):

    criterio = models.ForeignKey(Criterio, on_delete=models.SET_NULL, null=True)

    FIRST_ITEM_CHOICE = [
        ("Aulas colaborativas donde los docentes comparten la autoridad con los estudiantes de maneras muy específicas.", "1"),
        ("Aprendizaje Virtual como parte del desarrollo de la auto gestión y el auto desarrollo", "2"),
    ]

    numeral = models.CharField (max_length=1000, choices= FIRST_ITEM_CHOICE)
    
    FIRST_SUB_ITEM_CHOICE = [
        ("Los estudiantes deben desenvolverse bien en el trabajo en equipo de forma virtual", "2.1"),
    ]

    sub_numeral = models.CharField (max_length= 500, choices=FIRST_SUB_ITEM_CHOICE)
    
    FIRST_ITEM_CHOICE = [
        ("Aulas colaborativas donde los docentes comparten la autoridad con los estudiantes de maneras muy específicas.", "1"),
        ("Aprendizaje Virtual como parte del desarrollo de la auto gestión y el auto desarrollo", "2"),
    ]

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