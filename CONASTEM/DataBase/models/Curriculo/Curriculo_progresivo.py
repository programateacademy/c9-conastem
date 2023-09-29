from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.5 CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES

class CurriculoProgresivo(GeneralModel):

    ITEM_CHOICE = [
        ('2500', 'CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES'),
        ("2510", "Los equipos de profesores planean verticalmente la instrucción STEM dentro de la institución educativa."),
        ("2520", "El currículo está alineado con los estándares académicos actuales."),
        ("2530", "Las conexiones con las carreras relacionadas con las áreas STEM son una parte regular del currículo."),
        ("2540", "Se incluyen buenas prácticas de estándares internacionales que complementan y apoyan los estándares locales obligatorios."),
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
        super(CurriculoProgresivo, self).save(*args, **kwargs)

    def __str__(self):
        return self.numeral
