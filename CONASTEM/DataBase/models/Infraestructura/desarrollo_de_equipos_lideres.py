from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class DesarrolloDeEquiposLideres(GeneralModel):
    
    ITEM_CHOICE = [
        ("1110","El equipo de liderazgo de educación STEM está definido y nombrado en la institución para establecer monitorear y evaluar el programa completo."),
        ("1120","Los equipos de docentes abordan las expectativas específicas del programa establecido por el equipo líder."),
        ("1130","El equipo líder se reúne regularmente para discutir investigaciones, mejores prácticas, éxitos y oportunidades de mejora hacia los objetivos del Programa en Educación STEM."),
        ("1140","La toma de decisiones es realizada por todo el personal de la institución, el aula y los docentes de áreas especiales."),
        ("1150","El equipo líder establece un proceso de evaluación del Programa en Educación STEM de forma anual para medir los avances en los diferentes aspectos que componen esta transformación."), 
    ]

    code = models.CharField(max_length=4, default="1110")
    
    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    
    def __str__(self):
        return self.numeral