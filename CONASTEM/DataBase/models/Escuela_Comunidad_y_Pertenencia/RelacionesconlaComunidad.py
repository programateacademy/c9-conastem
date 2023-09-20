from django.db import models
from ..GeneralModel import GeneralModel

class RelacionesconlaComunidad(GeneralModel):

    ITEM_CHOICE =  ITEM_CHOICE = [
        ("5200","Relaciones con la Comunidad"),
        ("5210", "Los estudiantes tienen experiencias directas con profesionales de áreas STEM en entornos auténticos."),
        ("5220", "Las experiencias de campo y con profesionales invitados están integrados dentro de las actividades para aumentar el conocimiento de los estudiantes y ayudar en la selección de carrera."),
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]  # Modifica las opciones para incluir número y texto
        )
    codigo = models.CharField(
        max_length=4,  # Ajusta la longitud máxima según tus necesidades
    )
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(RelacionesconlaComunidad, self).save(*args, **kwargs)

    def __str__(self) :
        return self.numeral