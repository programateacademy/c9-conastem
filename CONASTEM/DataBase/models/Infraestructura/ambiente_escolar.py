from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class AmbienteEscolar(GeneralModel):

    ITEM_CHOICE = [
        ("1310","Aulas colaborativas donde los docentes comparten la autoridad con los estudiantes de maneras muy específicas."),
        ("1320","Aprendizaje Virtual como parte del desarrollo de la auto gestión y el auto desarrollo."),
        ("1330","La distribución de los salones de clase facilita la integración de asignaturas."),
        ("1340","Una cultura de investigación y creatividad."),
        ("1350","Desarrollo de las habilidades del Siglo XXI en cada clase."), 
        ("1360","Autonomía del estudiante es parte del diseño institucional."), 
    ]
    
    code = models.CharField(max_length=4, default="1310")
    
    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    
    SUB_ITEM_CHOICE = [
        ("1321","Los estudiantes deben desenvolverse bien en el trabajo en equipo de forma virtual."),
        ("1322","Los estudiantes deben conocer las herramientas electrónicas para trabajo en equipo virtual."),
        ("1361","El acceso al colegio debe ofrecerse durante todo el día."), 
        ("1362","Los estudiantes tienen tiempo disponible para realizar investigación y consultas a docentes."), 
    ]
    
    code = models.CharField(max_length=4, default="1321")
    
    sub_numeral = models.CharField(
        max_length= 1000,
        choices= SUB_ITEM_CHOICE
    )
    
    def __str__(self):
        return self.numeral
