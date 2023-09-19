from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel
class Sostenibilidad(GeneralModel):

    ITEM_CHOICE = [
        ("1710","Se cuenta con un plan de financiación estatal o privado que aporte al programa y cubra por lo menos cinco años del proyecto."),
        ("1720","El equipo líder cuenta con condiciones laborales y de infraestructura específicas que garantizan la proyección del programa a través de los años."),
        ("1730","El equipo líder asegura que todas las partes interesadas tengan oportunidades continuas para acceder a la información y aprender sobre la implementación de STEM."),
        ("1740","El Programa en Educación STEM estableció y monitorea los indicadores de gestión que miden el éxito del programa."),
        ("1750","El Programa en Educación STEM tiene establecido un proceso de auditoría interna/externa cada dos años."),
    ]
    
    code = models.CharField(max_length=4, default="1710")
    
    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )

    def __str__(self):
        return self.numeral