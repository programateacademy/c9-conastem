from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class ProfesionalesEspecializadosEducacionSTEM (GeneralModel):

    ITEM_CHOICE = [
        ("4000","Personal Docente y Adminstrativo"),
        ("4100","Profesionales Altamente Calificados Especializados en Edcuación STEM"),
        ("4110","Se han adoptado modelos que han sido probados, pilotados y aprobados."),
        ("4120","Todos los docentes tienen una carrera profesional en la institución"),
        ("4130","Los evaluadores del programa tienen experiencia en educación STEM"),
    ]
    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    codigo =models.CharField(max_length=7, default="4000")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(ProfesionalesEspecializadosEducacionSTEM, self).save(*args, **kwargs)

    def __str__(self) :
        return self.numeral