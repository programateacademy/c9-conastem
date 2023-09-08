from django.db import models
from ..GeneralModel import GeneralModel


class ConvivenciaEscolar (GeneralModel):

    ITEM_CHOICE = [
        ("531","Los estudiantes se tratan con confianza y respeto."),
        ("532","El docente facilita un ambiente positivo de aprendizaje social y emocional."),
        ("533","El personal del colegio enfatiza en el código de conducta y los valores."),
        ("534","El personal de la institución apoya las necesidades de todos los estudiantes."),
        ("535","Los estudiantes contribuyen en las decisiones de la institución.")
        ("536","Los estudiantes demuestran la aplicación del código de conducta y los valores.")
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    
    def __str__(self) :
        return self.numeral