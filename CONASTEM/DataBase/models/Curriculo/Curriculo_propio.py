from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.6 CURRÍCULO PROPIO

class CurriculoPropio(GeneralModel):

    ITEM_CHOICE = [
        ('2600', 'CURRÍCULO PROPIO'),
        ("2610", "El currículo es desarrollado por docentes o personas especializadas de la institución educativa, esto incluye la creación de actividades y proyectos."),
        ("2620", "El mejor aporte para un currículo en educación STEM será siempre aquel contenido creado por los propios profesores. Los profesores conocen sus estudiantes y saben qué temas y que aspectos les son interesantes y por eso pueden crear actividades y proyectos especiales para sus estudiantes."),
    ]

    numeral = models.CharField(
        max_length = 10000, 
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo = models.CharField(max_length=7, default='3000')
    def save(self, *args, **kwargs):
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break
        super(CurriculoPropio, self).save(*args, **kwargs)

    def __str__(self):
        return self.numeral
