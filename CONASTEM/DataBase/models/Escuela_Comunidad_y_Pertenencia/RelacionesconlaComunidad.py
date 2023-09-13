from django.db import models
from ..GeneralModel import GeneralModel


class RelacionesconlaCominudad (GeneralModel):

    ITEM_CHOICE = [
        ("521","Los estudiantes tienen experiencias directas con profesionales de áreas STEM en entornos auténticos."),
        ("522","Las experiencias de campo y con profesionales invitados están integrados dentro de las actividades para aumentar el conocimiento de los estudiantes y ayudar en la selección de carrera."),
        ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    
    def __str__(self) :
        return self.numeral