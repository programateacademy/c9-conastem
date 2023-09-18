from django.db import models
from ..GeneralModel import GeneralModel


class EstrategiasFormativas (GeneralModel):

    ITEM_CHOICE = [
        ("Estrategias formativas","3600"),
      	("Los estudiantes utilizan el proceso de diseño en ingeniería en la mayor parte de las actividades escolares y por lo tanto sus procesos formativos se dan siempre en equipo. Todo esto en la búsqueda de la solución de problemas (en ingeniería) y de respuestas (en ciencias).","3610"),
		("El docente sirve como facilitador a través de preguntas, las escucha y hace de guía de los estudiantes en el camino de su aprendizaje.","3620"),
		("Los profesores diseñan actividades basándose en las necesidades de los proyectos de los estudiantes.","3630"),
		("La instrucción apoya el discurso de los estudiantes a través de la redacción de informes y presentaciones orales, todos alineados con los estándares de su formación.","3640")
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    codigo =models.CharField(max_length=7, default="3600")
    def __str__(self) :
        return self.numeral