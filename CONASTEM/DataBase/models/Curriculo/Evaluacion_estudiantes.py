from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.8 EVALUACIÓN DE LOS ESTUDIANTES
class EvaluacionEstudiantes(GeneralModel):

    ITEM_CHOICE = [
        ('2800', 'EVALUACIÓN DE LOS ESTUDIANTES'),
        ("2810", "El currículo incluye actividades para que los docentes usen evaluaciones basadas en el desempeño para determinar el aprendizaje de los estudiantes."),
        ("2820", "Las evaluaciones previas / posteriores se utilizan para mostrar el desarrollo académico de los estudiantes."),
        ("2830", "Se diseñan las actividades para que los profesores observen y monitoreen el diálogo entre los estudiantes para evaluar los procesos en la resolución de problemas y la innovación."),
        ("2840", "Se diseñan las actividades para que los estudiantes participen en la autoevaluación y el establecimiento de metas."),
        ("2850", "La institución utiliza datos de evaluaciones estatales y escolares para impulsar las decisiones de la formación."),
        ("2860", "Evaluación continua. Tipología de evaluación donde los alumnos son examinados continuamente."),
        ("2870", "Asesoramiento personalizado. Tipología de evaluación enmarcada para demostrar si los alumnos han alcanzado objetivos educativos específicos, de acuerdo con su desarrollo personal."),
]

    numeral = models.CharField(
        max_length = 10000, 
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo = models.CharField(max_length=7, default='3000')
    def save(self, *args, **kwargs):
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break
        super(EvaluacionEstudiantes, self).save(*args, **kwargs)

    def __str__(self):
        return self.numeral
