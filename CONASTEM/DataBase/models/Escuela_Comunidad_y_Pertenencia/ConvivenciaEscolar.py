from django.db import models
from ..GeneralModel import GeneralModel


class ConvivenciaEscolar (GeneralModel):

    ITEM_CHOICE = [
        ("531","Los miembros de la comunidad son socios en el liderazgo del Programa en Educación STEM, evaluación de necesidades y guía de ayuda para la institución."),
        ("532","El programa ha incluido a diversos socios para guiar el trabajo en la institución."),
        ("533","Existen oportunidades para presentar el trabajo de los estudiantes a través de eventos comunitarios a través de exposiciones en el sitio o en línea."),
        ("534","La institución recopila y utiliza los comentarios de los padres / la comunidad para evaluar el progreso de la implementación del Programa en Educación STEM."),
        ("535","La escuela proporciona oportunidades de sensibilización comunitaria para los padres. Hay comunicación permanente a los padres de familia.")
        ("536","")
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    
    def __str__(self) :
        return self.numeral