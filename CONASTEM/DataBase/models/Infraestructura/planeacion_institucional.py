from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class PlaneacionInstitucional(GeneralModel):

    ITEM_CHOICE = [
        ("1210","Colaboración entre docentes consistente. La institución auspicia el trabajo colaborativo entre grupos de docentes desde la planeación de unidades y actividades hasta la ejecución en el aula."),
        ("1220","La Integración entre asignaturas es fundamental para el desarrollo académico. La institución considera fundamental la actividad interdisciplinaria para el Programa en Educación STEM."),
        ("1230","La organización considera el tiempo suficiente para los proyectos. Se han hecho modificaciones en los horarios y las intensidades horarias de las asignaturas, así como en el currículo para dar espacio a la ejecución de proyectos en los diferentes grados escolares."),
        ("1240","Hay un Programa en Educación STEM estructurado y en marcha, conducido por el equipo líder y avalado por la dirección de la institución educativa"),
        ("1250","Las directivas de la institución consideran el Programa en Educación STEM como central respecto a la estrategia para los próximos 4 a 6 años."),
    ]
    
    code = models.CharField(max_length=4, default="1210")

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )

    def __str__(self):
        return self.numeral