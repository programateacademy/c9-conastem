from django.db import models
from ..GeneralModel import GeneralModel


class SostenibilidadEscuelaComunidadyPertenencia (GeneralModel):

    ITEM_CHOICE = [
        ("Sostenibilidad-Escuela, Comunidad y Pertenencia","5.4.0.0"),
        ("Se mantienen relaciones de cooperación de la empresa privada, entidades educativas y universidades para lograr las experiencias profesionales que requieren los estudiantes en su proceso de selección de carrera.", "5.4.1.0"),
        ("Se establecen nuevas relaciones con la comunidad y se mantienen las antiguas para garantizar el liderazgo de la comunidad en el Programa en Educación STEM.", "5.4.2.0"),
        ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    codigo =models.CharField(max_length=7, default="5.4.0.0")
    
    def __str__(self) :
        return self.numeral