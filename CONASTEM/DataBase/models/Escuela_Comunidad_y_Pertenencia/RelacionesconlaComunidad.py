from django.db import models
from ..GeneralModel import GeneralModel


class RelacionesconlaCominudad (GeneralModel):

    ITEM_CHOICE = [
        ("Relaciones con la Comunidad","5.2.0.0"),
        ("Los estudiantes tienen experiencias directas con profesionales de áreas STEM en entornos auténticos.","5.2.1.0"),
        ("Las experiencias de campo y con profesionales invitados están integrados dentro de las actividades para aumentar el conocimiento de los estudiantes y ayudar en la selección de carrera.","5.2.2.0"),
        ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    codigo =models.CharField(max_length=7, default="5.2.0.0")
    def __str__(self) :
        return self.numeral