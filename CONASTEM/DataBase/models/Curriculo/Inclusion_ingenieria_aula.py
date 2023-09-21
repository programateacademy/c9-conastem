from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.2 INCLUSION DE LA INGENIERIA EN EL AULA
class InclusionIngenieriaAula(GeneralModel):

    ITEM_CHOICE = [
        ('2200', 'INCLUSIÓN DE LA INGENIERÍA EN EL AULA'),
        ("2210", "Inclusión del proceso de diseño en ingeniería en el currículo."),
        ("2220", "Los docentes de la mayoría de las asignaturas adoptan el proceso de diseño como parte fundamental del desarrollo pedagógico."),
        ("2230", "El proceso de diseño se ejecuta de forma intencional dado el potencial pedagógico de cada una de sus fases."),
        ("2240", "Las actividades se diseñan con el objetivo de incluir el pensamiento computacional y el pensamiento matemático en la gran mayoría de las asignaturas."),
        ("2250", "Actividades de prototipado en espacios para la creatividad (Maker Spaces)"),
    ]

    numeral = models.CharField(
        max_length = 10000, 
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
    )

    codigo = models.CharField(max_length=7, default='3000')
    def save(self, *args, **kwargs):
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                break
        super(InclusionIngenieriaAula, self).save(*args, **kwargs)

    def __str__(self):
        return self.numeral
