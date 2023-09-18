from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class ProfesionalesAltamenteCalificadosEspecializadosenEducacionSTEM (GeneralModel):

    ITEM_CHOICE = [
        ("411","Se han adoptado modelos que han sido probados, pilotados y aprobados."),
        ("412","Todos los docentes tienen una carrera profesional en la institución"),
        ("413","Los evaluadores del programa tienen experiencia en educación STEM"),
    ]

    numeral = models.CharField(
        max_length= 5000,
        choices= ITEM_CHOICE
        )

    
    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("ProfesionalesAltamenteCalificadosEspecializadosenEducacionSTEM", args={str(self.id)})