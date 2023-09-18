from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class SostenibilidadPersonalDocenteyAdministrativo (GeneralModel):

    ITEM_CHOICE = [
        ("441","Se dispone de un plan para la contratación que garantiza una selección de nuevos, docentes y/o personal administrativo que tenga el deseo de participar en el Programa en Educación STEM y aprender de forma continua en temas relevantes al programa"),
        ("442","La formación profesional continua para docentes nuevos y en servicio es parte de la política institucional, que contribuye a la sostenibilidad del Programa en Educación STEM."),
    ]

    numeral = models.CharField(
        max_length= 5000,
        choices= ITEM_CHOICE
        )

    
    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("SostenibilidadPersonalDocenteyAdministrativo", args={str(self.id)})