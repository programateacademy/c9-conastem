from datetime import timezone
from django.db import models
from django.urls import reverse

from ..Person_Responsable import PersonResponsable
from ..GeneralModel import GeneralModel

# 2.9 SOSTENBILIDAD - CURRÍCULO
class SostenibilidadCurriculo(GeneralModel):

    ITEM_CHOICE = [
        ("2.9.1", "Mantener el currículo acorde a las necesidades del campo laboral futuro de los estudiantes y hacer los cambios necesarios para su correcta adaptación."),
        ("2.9.2", "A través del proceso de evaluación del Programa en Educación STEM se deberá hacer los cambios o actualizaciones al currículo para dar a los estudiantes aporte efectivo en su aprendizaje en educación STEM."),
        ("2.9.3", "La organización de la institución educativa incluye dentro de su organización un especialista en currículo. Para ello debe estar nominado y operando activamente dentro del Programa en Educación STEM."),
    ]

    person_responsable = models.ManyToManyField(PersonResponsable, help_text="Seleccione un responsable", default=None)

    numeral = models.CharField(
        max_length=1000, 
        choices=ITEM_CHOICE
    )

    def __str__(self):
        return self.numeral

    def get_absolute_url(self):
        return reverse("SostenibilidadCurriculo", args=[str(self.id)])
