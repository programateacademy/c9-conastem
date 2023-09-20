from django.db import models
from ..GeneralModel import GeneralModel


class EstrategiasFormativas (GeneralModel):

    ITEM_CHOICE = [
        ("3600","Estrategias formativas"),
      	("3610","Los estudiantes utilizan el proceso de diseño en ingeniería en la mayor parte de las actividades escolares y por lo tanto sus procesos formativos se dan siempre en equipo. Todo esto en la búsqueda de la solución de problemas (en ingeniería) y de respuestas (en ciencias)."),
		("3620","El docente sirve como facilitador a través de preguntas, las escucha y hace de guía de los estudiantes en el camino de su aprendizaje."),
		("3630","Los profesores diseñan actividades basándose en las necesidades de los proyectos de los estudiantes."),
		("3640","La instrucción apoya el discurso de los estudiantes a través de la redacción de informes y presentaciones orales, todos alineados con los estándares de su formación.")
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

        super(EstrategiasFormativas, self).save(*args, **kwargs)

    def __str__(self) :
        return self.numeral