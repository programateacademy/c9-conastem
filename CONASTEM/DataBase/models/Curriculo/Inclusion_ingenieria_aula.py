from datetime import timezone
from django.db import models
from django.urls import reverse

from ..Person_Responsable import PersonResponsable
from ..GeneralModel import GeneralModel

# 2.2 INCLUSION DE LA INGENIERIA EN EL AULA
class Inclusion_ingenieria_aula(GeneralModel):

    ITEM_CHOICE = [
        ("221", "Inclusión del proceso de diseño en ingeniería en el currículo."),
        ("222", "Los docentes de la mayoría de las asignaturas adoptan el proceso de diseño como parte fundamental del desarrollo pedagógico."),
        ("223", "El proceso de diseño se ejecuta de forma intencional dado el potencial pedagógico de cada una de sus fases."),
        ("224", "Las actividades se diseñan con el objetivo de incluir el pensamiento computacional y el pensamiento matemático en la gran mayoría de las asignaturas."),
        ("225", "Actividades de prototipado en espacios para la creatividad (Maker Spaces)"),
    ]

    person_responsable = models.ManyToManyField(PersonResponsable, help_text="Seleccione un responsable", default=None)

    numeral = models.CharField(
        max_length=1000, 
        choices=ITEM_CHOICE
    )

    def __str__(self):
        return self.numeral

    def get_absolute_url(self):
        return reverse("Inclusion_ingenieria_aula", args=[str(self.id)])
