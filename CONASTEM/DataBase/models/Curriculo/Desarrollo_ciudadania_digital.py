from datetime import timezone
from django.db import models
from django.urls import reverse

from ..Person_Responsable import PersonResponsable
from ..GeneralModel import GeneralModel

# 2.3 DESARROLLO DE UNA CIUDADANÍA DIGITAL
class Desarrollo_ciudadania_digital(GeneralModel):

    ITEM_CHOICE = [
        ("231", "Establecimiento de una alfabetización digital como parte del entendimiento y el alcance de los desarrollos dentro de la 4a revolución industrial."),
        ("232", "Integración del mundo real al mundo virtual y su relación con la vida personal y laboral."),
        ("233", "Integración constante de nuevos desarrollos digitales dentro de actividades curriculares."),
        ("234", "Desarrollo de hábitos de aprendizaje continuo sobre nuevas alternativas y soluciones que aparecen dentro del mundo digital con miras al conocimiento crítico como consumidor y productor digital."),
    ]

    person_responsable = models.ManyToManyField(PersonResponsable, help_text="Seleccione un responsable", default=None)

    numeral = models.CharField(
        max_length=1000, 
        choices=ITEM_CHOICE
    )

    def __str__(self):
        return self.numeral

    def get_absolute_url(self):
        return reverse("Desarrollo_ciudadania_digital", args=[str(self.id)])
