from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 4.4 SOSTENIBILIDAD - PERSONAL DOCENTE Y ADMINISTRATIVO

class SostenibilidadDocenteAdministrativo (GeneralModel):

    ITEM_CHOICE = [
        ("4400","SOSTENIBILIDAD - PERSONAL DOCENTE Y ADMINISTRATIVO"),
        ("4410","Se dispone de un plan para la contratación que garantiza una selección de nuevos, docentes y/o personal administrativo que tenga el deseo de participar en el Programa en Educación STEM y aprender de forma continua en temas relevantes al programa"),
        ("4420","La formación profesional continua para docentes nuevos y en servicio es parte de la política institucional, que contribuye a la sostenibilidad del Programa en Educación STEM."),
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    codigo =models.CharField(max_length=7, default="4400")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(SostenibilidadDocenteAdministrativo, self).save(*args, **kwargs)

    
    def __str__(self) :
        return self.numeral