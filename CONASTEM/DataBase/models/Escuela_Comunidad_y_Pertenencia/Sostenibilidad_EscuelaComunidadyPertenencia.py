from django.db import models
from ..GeneralModel import GeneralModel


class SostenibilidadEscuelaComunidadyPertenencia (GeneralModel):

    ITEM_CHOICE = [
        ("541","Se mantienen relaciones de cooperación de la empresa privada, entidades educativas y universidades para lograr las experiencias profesionales que requieren los estudiantes en su proceso de selección de carrera."),
        ("542","Se establecen nuevas relaciones con la comunidad y se mantienen las antiguas para garantizar el liderazgo de la comunidad en el Programa en Educación STEM."),
        ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    
    def __str__(self) :
        return self.numeral