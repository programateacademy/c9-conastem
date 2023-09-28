from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 1.1 DESARROLLO DE EQUIPOS LÍDERES

class DesarrolloDeEquiposLideres(GeneralModel):
    
    ITEM_CHOICE = [
        ("1000","INFRAESTRUCTURA"),
        ("1100","DESARROLLO DE EQUIPOS LIDERES"),
        ("1110","El equipo de liderazgo de educación STEM está definido y nombrado en la institución para establecer monitorear y evaluar el programa completo."),
        ("1120","Los equipos de docentes abordan las expectativas específicas del programa establecido por el equipo líder."),
        ("1130","El equipo líder se reúne regularmente para discutir investigaciones, mejores prácticas, éxitos y oportunidades de mejora hacia los objetivos del Programa en Educación STEM."),
        ("1140","La toma de decisiones es realizada por todo el personal de la institución, el aula y los docentes de áreas especiales."),
        ("1150","El equipo líder establece un proceso de evaluación del Programa en Educación STEM de forma anual para medir los avances en los diferentes aspectos que componen esta transformación."), 
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo =models.CharField(max_length=7, default="1000")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]

                break

        super(DesarrolloDeEquiposLideres, self).save(*args, **kwargs)

    
    def __str__(self) :
        return self.numeral