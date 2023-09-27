from django.db import models
from ..GeneralModel import GeneralModel


class ConvivenciaEscolar (GeneralModel):

    ITEM_CHOICE = [
        ("5300","CONVIVENCIA ESCOLAR"),
        ("5310","Los estudiantes se tratan con confianza y respeto."),
        ("5320","El docente facilita un ambiente positivo de aprendizaje social y emocional."),
        ("5330","El personal del colegio enfatiza en el código de conducta y los valores."),
        ("5340","El personal de la institución apoya las necesidades de todos los estudiantes."),
        ("5350","Los estudiantes contribuyen en las decisiones de la institución."),
        ("5360","Los estudiantes demuestran la aplicación del código de conducta y los valores.")
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    codigo =models.CharField(max_length=7, default="5300")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(ConvivenciaEscolar, self).save(*args, **kwargs)

    
    def __str__(self) :
        return self.numeral