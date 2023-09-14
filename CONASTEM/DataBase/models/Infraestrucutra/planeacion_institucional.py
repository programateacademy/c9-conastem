from django.db import models
from django.db.models import F, Q, When
from ..Person_Responsable import PersonResponsable
from ...models.Criterio import Criterio

class PlaneacionInstitucional(models.Model):

    criterio = models.ForeignKey(Criterio, on_delete=models.SET_NULL, null=True)

    ITEM_CHOICE = [
        ("Colaboración entre docentes consistente. La institución auspicia el trabajo colaborativo entre grupos de docentes desde la planeación de unidades y actividades hasta la ejecución en el aula.", "1"),
        ("La Integración entre asignaturas es fundamental para el desarrollo académico. La institución considera fundamental la actividad interdisciplinaria para el Programa en Educación STEM.", "2"),
        ("La organización considera el tiempo suficiente para los proyectos. Se han hecho modificaciones en los horarios y las intensidades horarias de las asignaturas, así como en el currículo para dar espacio a la ejecución de proyectos en los diferentes grados escolares.", "3"),
        ("Hay un Programa en Educación STEM estructurado y en marcha, conducido por el equipo líder y avalado por la dirección de la institución educativa", "4"),
        ("Las directivas de la institución consideran el Programa en Educación STEM como central respecto a la estrategia para los próximos 4 a 6 años.", "5"),
    ]
    
    numeral = models.CharField (max_length=1000, choices= ITEM_CHOICE)
    
    PRIORITY_MODEL_CHOICE = (
        (" ", "Exploratorio"),
        (" ", "Introductorio"),
        ("", "Inmerción parcial"),
        (" ", "Inmerción completa"),
    )

    priority_model = models.CharField (max_length=4, choices= PRIORITY_MODEL_CHOICE, default= "Introductorio")
    
    dep_responsable = models.CharField (max_length=30, default= "Dirección")
    
    person_responsable = models.ManyToManyField(PersonResponsable, help_text= "Seleccione un responsable")
    
    track_year = models.IntegerField (help_text="Ingrese año de seguimiento")
    
    track_date = models.CharField(max_length=5, help_text="Ingrese fecha de seguimiento")
    
    internal_auditory_date = models.DateField(default="31/01/2000", null= True)
    internal_auditory_obs = models.TextField(max_length=1000, blank= True)

    external_auditory_date = models.DateField(default="31/01/2000", null= True, blank= True)
    external_auditory_obs = models.TextField(max_length=1000, blank= True)

    def __str__(self):
        return self.numeral