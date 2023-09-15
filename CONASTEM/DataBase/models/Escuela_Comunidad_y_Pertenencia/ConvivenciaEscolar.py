from django.db import models
from ..GeneralModel import GeneralModel


class ConvivenciaEscolar (GeneralModel):

    ITEM_CHOICE = [
        ("Convivencia Escolar","5.3.0.0"),
        ("Los estudiantes se tratan con confianza y respeto.","5.3.1.0"),
        ("El docente facilita un ambiente positivo de aprendizaje social y emocional.","5.3.2.0"),
        ("El personal del colegio enfatiza en el código de conducta y los valores.","5.3.3.0"),
        ("El personal de la institución apoya las necesidades de todos los estudiantes.","5.3.4.0"),
        ("Los estudiantes contribuyen en las decisiones de la institución.","5.3.5.0"),
        ("Los estudiantes demuestran la aplicación del código de conducta y los valores.","5.3.6.0")
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    codigo =models.CharField(max_length=7, default="5.3.0.0")
    
    def __str__(self) :
        return self.numeral