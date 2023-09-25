from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class ApoyoPedagogico(GeneralModel):

    ITEM_CHOICE = [
        ("4300","APOYO PEDAGÓGICO PARA EL PERSONAL"),
        ("4310","Hay un sistema de evaluación docente en servicio para premiar el esfuerzo de los profesores dentro del Programa en Educación STEM"),
        ("4320","La institución aporta realimentación y observaciones frecuentemente a los docentes con respecto a su desempeño dentro del programa en educación STEM."),       
        ("4330","La institución educativa utiliza protocolos de observación validados en el aula."),
        ("4340","Los docentes en educación STEM participan en sesiones de desarrollo profesional de todo el grupo, enfocadas en el desarrollo del currículo integrado, para construir conocimiento de contenido y pedagógico efectivo (por ejemplo, Aprendizaje Basado en Lecciones e investigación)"),
        ("4350","Los profesores del Programa en Educación STEM observan a sus colegas y se involucran en la reflexión formal y la discusión sobre las prácticas"),
        ("4360","Las sesiones de desarrollo profesional se alinean con las necesidades del programa y de la institución educativa y las necesidades de aprendizaje de los estudiantes."),
        ("4370","Los docentes son evaluados constantemente con respecto al conocimiento del contenido propio de su área, mediante el uso de evaluaciones formales o revisiones de desempeño"),
        ("4380","Se desarrollan e implementan planes de desarrollo profesional individualizados para respaldar el conocimiento mejorado del contenido"),
        ]
    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    codigo =models.CharField(max_length=7, default="4300")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(ApoyoPedagogico, self).save(*args, **kwargs)
    def __str__(self) :
        return self.numeral