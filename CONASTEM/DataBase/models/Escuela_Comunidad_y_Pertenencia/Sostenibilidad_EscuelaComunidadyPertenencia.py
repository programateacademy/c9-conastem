from django.db import models
from ..GeneralModel import GeneralModel


class SostenibilidadEscuelaComunidadyPertenencia (GeneralModel):

    ITEM_CHOICE = [
        ("5400","SOSTENIBILIDAD-ESCUELA, COMUNIDAD Y COMPROMISO"),
        ("5410","Se mantienen relaciones de cooperación de la empresa privada, entidades educativas y universidades para lograr las experiencias profesionales que requieren los estudiantes en su proceso de selección de carrera."),
        ("5420","Se establecen nuevas relaciones con la comunidad y se mantienen las antiguas para garantizar el liderazgo de la comunidad en el Programa en Educación STEM."),
        ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    codigo =models.CharField(max_length=4)
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(SostenibilidadEscuelaComunidadyPertenencia, self).save(*args, **kwargs)

    
    def __str__(self) :
        return self.numeral