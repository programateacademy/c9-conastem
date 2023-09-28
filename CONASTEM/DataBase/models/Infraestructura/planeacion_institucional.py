from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 1.2 PLANEACIÓN INSTITUCIONAL

class PlaneacionInstitucional(GeneralModel):

    ITEM_CHOICE = [
        ("1200","PLANEACIÓN INSTITUCIONAL"),
        ("1210","Colaboración entre docentes consistente. La institución auspicia el trabajo colaborativo entre grupos de docentes desde la planeación de unidades y actividades hasta la ejecución en el aula."),
        ("1220","La Integración entre asignaturas es fundamental para el desarrollo académico. La institución considera fundamental la actividad interdisciplinaria para el Programa en Educación STEM."),
        ("1230","La organización considera el tiempo suficiente para los proyectos. Se han hecho modificaciones en los horarios y las intensidades horarias de las asignaturas, así como en el currículo para dar espacio a la ejecución de proyectos en los diferentes grados escolares."),
        ("1240","Hay un Programa en Educación STEM estructurado y en marcha, conducido por el equipo líder y avalado por la dirección de la institución educativa"),
        ("1250","Las directivas de la institución consideran el Programa en Educación STEM como central respecto a la estrategia para los próximos 4 a 6 años."),
    ]
    
    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo =models.CharField(max_length=7, default="1200")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(PlaneacionInstitucional, self).save(*args, **kwargs)

    
    def __str__(self) :
        return self.numeral