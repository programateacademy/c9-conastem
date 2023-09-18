from django.db import models
from ..GeneralModel import GeneralModel

class RelacionesconlaComunidad(GeneralModel):

    ITEM_CHOICE = {
        "Relaciones con la Comunidad":"5200",
        "Los estudiantes tienen experiencias directas con profesionales de áreas STEM en entornos auténticos.":"5210",
        "Las experiencias de campo y con profesionales invitados están integrados dentro de las actividades para aumentar el conocimiento de los estudiantes y ayudar en la selección de carrera.":"5220",
    }

    numeral = models.CharField(
        max_length= 10000,
        choices=[(texto, texto) for texto in ITEM_CHOICE.keys()],
        )
    codigo = models.CharField(
        max_length=4,  # Ajusta la longitud máxima según tus necesidades
        verbose_name="Código del Item",
    )
    def __str__(self) :
        return self.numeral