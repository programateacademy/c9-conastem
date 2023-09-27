from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel


class AmbienteEscolar (GeneralModel):

    ITEM_CHOICE = [
        ("1300","Ambiente escolar"),
        ("1310","Aulas colaborativas donde los docentes comparten la autoridad con los estudiantes de maneras muy específicas."),
        ("1320","Aprendizaje Virtual como parte del desarrollo de la auto gestión y el auto desarrollo."),
        ("1321","Los estudiantes deben desenvolverse bien en el trabajo en equipo de forma virtual."),
        ("1330","La distribución de los salones de clase facilita la integración de asignaturas."),
        ("1340","Una cultura de investigación y creatividad."),
        ("1350","Desarrollo de las habilidades del Siglo XXI en cada clase."), 
        ("1360","Autonomía del estudiante es parte del diseño institucional."), 
        ("1361","El acceso al colegio debe ofrecerse durante todo el día."),
        ("1362","Los estudiantes tienen tiempo disponible para realizar investigación y consultas a docentes."), 
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo =models.CharField(max_length=7, default="1300")
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(AmbienteEscolar, self).save(*args, **kwargs)

    def __str__(self) :
        return self.numeral