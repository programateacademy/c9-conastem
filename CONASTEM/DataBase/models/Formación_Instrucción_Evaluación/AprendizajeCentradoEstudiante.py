from django.db import models
from ..GeneralModel import GeneralModel


class AprendizajeCentrado (GeneralModel):

    ITEM_CHOICE = [
        ("Formación/Instrucción basada en Aprendizaje Basado en Lecciones / Aprendizaje Basado en Proyectos / Aprendizaje enfocado en la indagación.", "3.1.1"),
        ("El aprendizaje es centrado en el estudiante. La dinámica de aula y en general en la institución se prevé el tiempo para investigación y trabajo en equipo, así como de tiempo de consulta a los profesores en tiempo fuera del horario de la asignatura.", "3.1.2"),
        ("Los proyectos son centrales al currículo. Los objetivos de los proyectos serán la meta más importante para lograr aprobar el grado escolar.", "3.1.3"),
        ("Dentro de las experiencias de aula predominarán los retos de ingeniería como parte del ABP-ABL.", "3.1.4"),
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    
    SUB_NUMERAL_CHOICE = [
        ("3.1.2.1","Autonomía del estudiante"),
        ("3.1.2.2", "Los estudiantes descubren qué lo que están aprendiendo es importante para su vida y su comunidad."),
        ("3.1.2.3", "Los estudiantes le dan importancia y relevancia a las actividades que se hacen durante sus clases. Toman control sobre el desarrollo del aprendizaje."),
        ("3.1.2.4", "Los estudiantes demuestran su conocimiento sobre las áreas STEM y que son base de una formación en educación STEM"),
    ]
    
    def __str__(self) :
        return self.numeral