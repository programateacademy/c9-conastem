from django.db import models
from ..GeneralModel import GeneralModel


class AprendizajeCentrado (GeneralModel):

    ITEM_CHOICE = [
        ("Todos los estudiantes reciben acceso equitativo a la formación y a los programas. No se selecciona únicamente a los estudiantes con gusto por las asignaturas S.T.E.M., todos los estudiantes hacen parte del programa", "1"),
        ("Todos los estudiantes con necesidades específicas e identificadas están siendo ubicados para facilitar su adaptación. Aprendizaje individualizado.", "2"),
        ("Se han diseñado acciones o planes especiales para alentar a los estudiantes con bajo interés o desempeño a desarrollar interés en las carreras STEM.", "3"),
        ("Los docentes reciben desarrollo profesional sobre las diferencias culturales y de género para enriquecer la formación.", "4"),
        ("El aula STEM se diferencia en ubicar a todos los estudiantes, con una consideración especial hacia todos los grupos geográficos, socioeconómicos, raciales, étnicos y de género.", "5"),
        ("La institución está preparada para proveer una formación incluyente. Promueve las oportunidades de aprendizaje para todos los estudiantes, pero respeta las diferencias culturales y de género.", "6"),
    ]

    numeral = models.CharField(
        max_length= max(len(ITEM_CHOICE)),
        choices= ITEM_CHOICE
        )