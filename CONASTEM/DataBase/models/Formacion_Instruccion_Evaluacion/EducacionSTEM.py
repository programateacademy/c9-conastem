from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class EducacionSTEMIntegrada (GeneralModel):

    ITEM_CHOICE = [
        ('3400', 'EDUCACIÓN STEM INTEGRADA'),
        ('3410', 'Todos los profesores integran diseño en ingeniería, aplicaciones tecnológicas, investigación y análisis matemático. Evidencia de educación STEM integrada en todas las aulas.'),
        ('3411', 'Retos de ingeniería incluidos en las actividades.'),
        ('3412', 'Los estudiantes aprenden de las fallas o fracasos en el diseño, tienen la oportunidad de rediseñar y consideran "fallar" como parte cotidiana en el proceso de diseño.'),
        ('3420', 'Los contenidos de las actividades han sido diseña con base en una propuesta de currículo que incluye problemas del mundo real y de situaciones que le son relevantes a los estudiantes.'),
        ('3421', 'Los contextos de las actividades y proyectos involucran a los estudiantes dada la relevancia de éstos.'),
        ('3422', 'La selección de temas considera los intereses de los estudiantes, así como aquellos asuntos de mayor relevancia para la comunidad.'),
        ('3430', 'Las actividades se deseñan con una pedagogía centrada en el estudiante.'),
        ('3440', 'Las actividades se desarrollan enfocadas al trabajo en equipo y la colaboración entre los estudiantes.'),
        ('3450', 'Las actividades se diseñan con una base fundamental de ciencias y matemáticas e incluyendo en lo posibles otras áreas del currículo.')
    ]

    numeral = models.CharField(
        max_length= 200,
        choices= ITEM_CHOICE
    )