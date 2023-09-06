from django.db import models
from models.Criterio import Criterio
from models.Person_Responsable import PersonResponsable
from models.Auditory import Auditory


class AprendizajeCentrado (models.Model):

    criterio = models.ForeignKey (Criterio, on_delete=models.SET_NULL, null=True, default= "INFRAESTRUCTURA")

    numeral = models


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
    
    auditory = models.ForeignKey(Auditory, null= True, on_delete=models.SET_NULL)