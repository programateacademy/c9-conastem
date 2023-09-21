from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales (GeneralModel):

    ITEM_CHOICE = [
        ("4200","DESARROLLO PROFESIONAL INICIAL Y CONTINUO PARA DOCENTES, DIRECTORES DE ESCUELA Y CONSEJEROS PROFESIONALES"),
        ("4210","La organización tiene previsto el desarrollo profesional de docentes y está implementado en la institución educativa"),
        ("4220","Los docentes tienen la oportunidad de escoger planes de desarrollo individuales de educación superior."),       
        ("4230","La formación profesional incluye apoyo del tipo pedagógico durante el año escolar y también durante la puesta en marcha de estrategias en educación STEM implementadas en la institución educativa."),
        ("4240","Los docentes reciben 40 o más horas de formación profesional por año."),
        ("4250","Expertos en contenido proporcionan desarrollo profesional para los profesores"),
        ("4260","Los docentes hacen parte de planes de formación de postgrado para la creación de nuevos contenidos."),
        ]
    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    codigo =models.CharField(max_length=7, default="4200")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales, self).save(*args, **kwargs)
    def __str__(self) :
        return self.numeral