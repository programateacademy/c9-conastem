from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class ApoyoPedagogico(GeneralModel):

    ITEM_CHOICE = [
        ("431","Hay un sistema de evaluación docente en servicio para premiar el esfuerzo de los profesores dentro del Programa en Educación STEM"),
        ("432","La institución aporta realimentación y observaciones frecuentemente a los docentes con respecto a su desempeño dentro del programa en educación STEM."),       
        ("433","La institución educativa utiliza protocolos de observación validados en el aula."),
        ("434","Los docentes en educación STEM participan en sesiones de desarrollo profesional de todo el grupo, enfocadas en el desarrollo del currículo integrado, para construir conocimiento de contenido y pedagógico efectivo (por ejemplo, Aprendizaje Basado en Lecciones e investigación)"),
        ("435","Los profesores del Programa en Educación STEM observan a sus colegas y se involucran en la reflexión formal y la discusión sobre las prácticas"),
        ("436","Las sesiones de desarrollo profesional se alinean con las necesidades del programa y de la institución educativa y las necesidades de aprendizaje de los estudiantes."),
        ("437","Los docentes son evaluados constantemente con respecto al conocimiento del contenido propio de su área, mediante el uso de evaluaciones formales o revisiones de desempeño"),
        ("438","Se desarrollan e implementan planes de desarrollo profesional individualizados para respaldar el conocimiento mejorado del contenido"),
        ]
    numeral = models.CharField(
        max_length= 5000,
        choices= ITEM_CHOICE
        )
    
    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse ("ApoyoPedagogico", args={str(self.id)})