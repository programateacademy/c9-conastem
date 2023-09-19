from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class CompromisodelaComunidad (GeneralModel):

    ITEM_CHOICE = [
        ("Escuela, Comunidad y Pertenencia","5.0.0.0"),
        ("Compromiso de la comunidad","5.1.0.0"),
        ("Los miembros de la comunidad son socios en el liderazgo del Programa en Educación STEM, evaluación de necesidades y guía de ayuda para la institución.","5.1.1.0"),
        ("El programa ha incluido a diversos socios para guiar el trabajo en la institución.","5.1.2.0"),
        ("Existen oportunidades para presentar el trabajo de los estudiantes a través de eventos comunitarios a través de exposiciones en el sitio o en línea.","5.1.3.0"),
        ("La institución recopila y utiliza los comentarios de los padres / la comunidad para evaluar el progreso de la implementación del Programa en Educación STEM.","5.1.4.0"),
        ("La escuela proporciona oportunidades de sensibilización comunitaria para los padres. Hay comunicación permanente a los padres de familia.","5.1.5.0")
    ]

    numeral = models.CharField(
        max_length= 1000,
        choices= ITEM_CHOICE
        )
    
    codigo = models.CharField(max_length=7, default="5000")
    
    
    def __str__(self) :
        return self.numeral
    
