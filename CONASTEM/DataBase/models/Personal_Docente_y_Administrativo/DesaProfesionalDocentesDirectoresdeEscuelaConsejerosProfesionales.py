from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales (GeneralModel):

    ITEM_CHOICE = [
        ("421","La organización tiene previsto el desarrollo profesional de docentes y está implementado en la institución educativa"),
        ("422","Los docentes tienen la oportunidad de escoger planes de desarrollo individuales de educación superior."),       
        ("423","La formación profesional incluye apoyo del tipo pedagógico durante el año escolar y también durante la puesta en marcha de estrategias en educación STEM implementadas en la institución educativa."),
        ("424","Los docentes reciben 40 o más horas de formación profesional por año."),
        ("425","Expertos en contenido proporcionan desarrollo profesional para los profesores"),
        ("426","Los docentes hacen parte de planes de formación de postgrado para la creación de nuevos contenidos."),
        ]
    numeral = models.CharField(
        max_length= 5000,
        choices= ITEM_CHOICE
        )
    
    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales", args={str(self.id)})