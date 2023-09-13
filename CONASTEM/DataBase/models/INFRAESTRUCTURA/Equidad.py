from django.db import models
from django.db.models import F, Q, When
from ..GeneralModel import GeneralModel

# 1.5 Equidad
class Equidad(GeneralModel):

    ITEM_CHOICE = [
        ("Todos los estudiantes reciben acceso equitativo a la formación y a los programas. No se selecciona únicamente a los estudiantes con gusto por las asignaturas S.T.E.M., todos los estudiantes hacen parte del programa", "1"),
        ("Todos los estudiantes con necesidades específicas e identificadas están siendo ubicados para facilitar su adaptación. Aprendizaje individualizado.", "2"),
        ("Se han diseñado acciones o planes especiales para alentar a los estudiantes con bajo interés o desempeño a desarrollar interés en las carreras STEM.", "3"),
        ("Los docentes reciben desarrollo profesional sobre las diferencias culturales y de género para enriquecer la formación.", "4"),
        ("El aula STEM se diferencia en ubicar a todos los estudiantes, con una consideración especial hacia todos los grupos geográficos, socioeconómicos, raciales, étnicos y de género.", "5"),
        ("La institución está preparada para proveer una formación incluyente. Promueve las oportunidades de aprendizaje para todos los estudiantes, pero respeta las diferencias culturales y de género.", "6"),
    ]

    numeral = models.CharField (max_length=1000, choices= ITEM_CHOICE)

    SUB_ITEM_CHOICE = [
        ("Procesos claros desarrollados para la inducción de nuevos estudiantes.", "1"),
        ("Programa o actividades que garanticen una transición efectiva para los estudiantes.", "2"),
        ("La educación STEM es incluyente, y una forma importante es hacer que se sientan como en casa a través de actividades o de programas, con suficiente anterioridad para que puedan participar en la labor académica, no como extraños sino ya apropiados de las costumbres de los estudiantes veteranos.", "3"),
        ("La institución tiene por objetivo incrementar la participación de la mujer en las áreas STEM, de tal manera que la población estudiantil involucrada en el programa sea cada vez mayor. ", "4"),
    ]

    sub_numeral = models.CharField (max_length= 500, default="")


    def __str__(self):
        return self.numeral