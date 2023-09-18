from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class EducacionStemIntegrada (GeneralModel):

    ITEM_CHOICE = [
        ('3.4.1', 'Todos los profesores integran diseño en ingeniería, aplicaciones tecnológicas, investigación y análisis matemático. Evidencia de educación STEM integrada en todas las aulas.'),
        ('3.4.2', 'Los contenidos de las actividades han sido diseña con base en una propuesta de currículo que incluye problemas del mundo real y de situaciones que le son relevantes a los estudiantes.'),
        ('3.4.3', 'Las actividades se deseñan con una pedagogía centrada en el estudiante'),
        ('3.4.4', 'Las actividades se desarrollan enfocadas al trabajo en equipo y la colaboración entre los estudiantes'),
        ('3.4.5', 'Las actividades se diseñan con una base fundamental de ciencias y matemáticas e incluyendo en lo posibles otras áreas del currículo.')
    ]

    numeral = models.CharField(max_length=250, choices=ITEM_CHOICE)

    SUB_NUMERAL_1_CHOICE = [
        ('3.4.1.1', 'Retos de ingeniería incluidos en las actividades.'),
        ('3.4.1.2', 'Los estudiantes aprenden de las fallas o fracasos en el diseño, tienen la oportunidad de rediseñar y consideran "fallar" como parte cotidiana en el proceso de diseño.')
    ]

    sub_numeral_1 = models.CharField(max_length=180, choices=SUB_NUMERAL_1_CHOICE)

    SUB_NUMERAL_2_CHOICE = [
        ('3.4.2.1', 'Los contextos de las actividades y proyectos involucran a los estudiantes dada la relevancia de éstos.'),
        ('3.4.2.2', 'La selección de temas considera los intereses de los estudiantes, así como aquellos asuntos de mayor relevancia para la comunidad.')
    ]

    sub_numeral_2 = models.CharField(max_length=150, choices=SUB_NUMERAL_2_CHOICE)

    class Meta:
        verbose_name = ("Educación STEM integrada")
        verbose_name_plural = ("Educación STEM integrada")
    
    def __str__(self):
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("educacion_stem_integrada_detail", args=[str(self.id)])
    