from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class UsoDeInformacion(GeneralModel):

    ITEM_CHOICE = [
        ("1500","Uso de informacion"),
        ("1510","Uso de la información de pruebas estandarizadas estatales, además de otras evaluaciones."),
        ("1520","Seguimiento riguroso a la información de las evaluaciones formativas."),
        ("1530","Hay un proyecto de seguimiento del avance del programa con los estudiantes."),
        ("1540","Existe un plan individual de educación para cada estudiante."),
        ("1550","Se utilizan sistemas de protección y de seguimiento de la información."),
        ("1560","Los estudiantes y los padres tienen acceso a información."),
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo =models.CharField(max_length=7, default="1500")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                break

        super(UsoDeInformacion, self).save(*args, **kwargs)

    
    def __str__(self) :
        return self.numeral