from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.5 CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES
class CurriculoProgresivo(GeneralModel):

    ITEM_CHOICE = [
        ("251", "Los equipos de profesores planean verticalmente la instrucción STEM dentro de la institución educativa."),
        ("252", "El currículo está alineado con los estándares académicos actuales."),
        ("253", "Las conexiones con las carreras relacionadas con las áreas STEM son una parte regular del currículo."),
        ("254", "Se incluyen buenas prácticas de estándares internacionales que complementan y apoyan los estándares locales obligatorios."),
    ]

    numeral = models.CharField(
        max_length = 10000, 
        choices = ITEM_CHOICE
    )

    def __str__(self):
        return self.numeral
