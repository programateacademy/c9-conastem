from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class DesarrolloDeEquiposLideres(GeneralModel):
    
    ITEM_CHOICE = [
        ("111","El equipo de liderazgo de educación STEM está definido y nombrado en la institución para establecer monitorear y evaluar el programa completo."),
        ("112","Los equipos de docentes abordan las expectativas específicas del programa establecido por el equipo líder."),
        ("113","El equipo líder se reúne regularmente para discutir investigaciones, mejores prácticas, éxitos y oportunidades de mejora hacia los objetivos del Programa en Educación STEM."),
        ("114","La toma de decisiones es realizada por todo el personal de la institución, el aula y los docentes de áreas especiales."),
        ("115","El equipo líder establece un proceso de evaluación del Programa en Educación STEM de forma anual para medir los avances en los diferentes aspectos que componen esta transformación."), 
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    
    def __str__(self):
        return self.numeral