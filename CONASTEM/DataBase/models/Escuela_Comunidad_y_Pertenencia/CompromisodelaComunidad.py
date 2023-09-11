from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class CompromisodelaComunidad (GeneralModel):

    ITEM_CHOICE = [
        ("511","Los miembros de la comunidad son socios en el liderazgo del Programa en Educación STEM, evaluación de necesidades y guía de ayuda para la institución."),
        ("512","El programa ha incluido a diversos socios para guiar el trabajo en la institución."),
        ("513","Existen oportunidades para presentar el trabajo de los estudiantes a través de eventos comunitarios a través de exposiciones en el sitio o en línea."),
        ("514","La institución recopila y utiliza los comentarios de los padres / la comunidad para evaluar el progreso de la implementación del Programa en Educación STEM."),
        ("515","La escuela proporciona oportunidades de sensibilización comunitaria para los padres. Hay comunicación permanente a los padres de familia.")
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    
    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("CompromisodelaCominudad", args={str(self.id)})
    