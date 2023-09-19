from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class UsoDeInformacion(GeneralModel):

    ITEM_CHOICE = [
        ("1510","Uso de la información de pruebas estandarizadas estatales, además de otras evaluaciones."),
        ("1520","Seguimiento riguroso a la información de las evaluaciones formativas."),
        ("1530","Hay un proyecto de seguimiento del avance del programa con los estudiantes."),
        ("1540","Existe un plan individual de educación para cada estudiante."),
        ("1550","Se utilizan sistemas de protección y de seguimiento de la información."),
        ("1560","Los estudiantes y los padres tienen acceso a información."),
    ]

    code = models.CharField(max_length=4, default="1510")

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )

    def __str__(self):
        return self.numeral