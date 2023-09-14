from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.6 CURRÍCULO PROPIO
class CurriculoPropio(GeneralModel):

    ITEM_CHOICE = [
        ("261", "El currículo es desarrollado por docentes o personas especializadas de la institución educativa, esto incluye la creación de actividades y proyectos."),
        ("262", "El mejor aporte para un currículo en educación STEM será siempre aquel contenido creado por los propios profesores. Los profesores conocen sus estudiantes y saben qué temas y que aspectos les son interesantes y por eso pueden crear actividades y proyectos especiales para sus estudiantes."),
    ]

    numeral = models.CharField(
        max_length = 10000, 
        choices = ITEM_CHOICE
    )

    def __str__(self):
        return self.numeral
