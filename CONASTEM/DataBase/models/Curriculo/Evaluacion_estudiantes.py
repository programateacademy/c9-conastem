from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.8 EVALUACIÓN DE LOS ESTUDIANTES
class EvaluacionEstudiantes(GeneralModel):

    ITEM_CHOICE = [
        ("281", "El currículo incluye actividades para que los docentes usen evaluaciones basadas en el desempeño para determinar el aprendizaje de los estudiantes."),
        ("282", "Las evaluaciones previas / posteriores se utilizan para mostrar el desarrollo académico de los estudiantes."),
        ("283", "Se diseñan las actividades para que los profesores observen y monitoreen el diálogo entre los estudiantes para evaluar los procesos en la resolución de problemas y la innovación."),
        ("284", "Se diseñan las actividades para que los estudiantes participen en la autoevaluación y el establecimiento de metas."),
        ("285", "La institución utiliza datos de evaluaciones estatales y escolares para impulsar las decisiones de la formación."),
        ("286", "Evaluación continua. Tipología de evaluación donde los alumnos son examinados continuamente."),
        ("287", "Asesoramiento personalizado. Tipología de evaluación enmarcada para demostrar si los alumnos han alcanzado objetivos educativos específicos, de acuerdo con su desarrollo personal."),
]

    numeral = models.CharField(
        max_length = 10000, 
        choices = ITEM_CHOICE
    )

    def __str__(self):
        return self.numeral
