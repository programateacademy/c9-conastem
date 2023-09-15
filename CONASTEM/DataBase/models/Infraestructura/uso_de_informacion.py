from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class UsoDeInformacion(GeneralModel):

    ITEM_CHOICE = [
        ("151","Uso de la información de pruebas estandarizadas estatales, además de otras evaluaciones."),
        ("152","Seguimiento riguroso a la información de las evaluaciones formativas."),
        ("153","Hay un proyecto de seguimiento del avance del programa con los estudiantes."),
        ("154","Existe un plan individual de educación para cada estudiante."),
        ("155","Se utilizan sistemas de protección y de seguimiento de la información."),
        ("156","Los estudiantes y los padres tienen acceso a información."),
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )

    def __str__(self):
        return self.numeral