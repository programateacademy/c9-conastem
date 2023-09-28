from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 5.1 COMPROMISO DE LA COMUNIDAD

class CompromisodelaComunidad (GeneralModel):

    ITEM_CHOICE = [
        ("5000","ESCUELA, COMUNIDAD Y PERTENENCIA"),
        ("5100","COMPROMISO DE LA COMUNIDAD"),
        ("5110","Los miembros de la comunidad son socios en el liderazgo del Programa en Educación STEM, evaluación de necesidades y guía de ayuda para la institución."),
        ("5120","El programa ha incluido a diversos socios para guiar el trabajo en la institución."),
        ("5130","Existen oportunidades para presentar el trabajo de los estudiantes a través de eventos comunitarios a través de exposiciones en el sitio o en línea."),
        ("5140","La institución recopila y utiliza los comentarios de los padres / la comunidad para evaluar el progreso de la implementación del Programa en Educación STEM."),
        ("5150","La escuela proporciona oportunidades de sensibilización comunitaria para los padres. Hay comunicación permanente a los padres de familia.")
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo =models.CharField(max_length=7, default="5000")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(CompromisodelaComunidad, self).save(*args, **kwargs)

    
    def __str__(self) :
        return self.numeral
    
