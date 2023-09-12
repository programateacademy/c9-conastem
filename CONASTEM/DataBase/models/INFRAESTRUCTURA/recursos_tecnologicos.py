from django.db import models
from django.db.models import F, Q, When
from ..Person_Responsable import PersonResponsable
from ...models.Criterio import Criterio

class Equidad(models.Model):

    criterio = models.ForeignKey(Criterio, on_delete=models.SET_NULL, null=True)

    ITEM_CHOICE = [
        ("Las necesidades tecnológicas de los estudiantes y el personal se identifican y abordan como parte del diseño del programa", "1"),
        ("Las compras de tecnología están completas o incluidas en un presupuesto futuro", "2"),
        ("Los profesores y los estudiantes tienen acceso a la solicitud de mantenimiento o apoyo para el uso de la tecnología de instrucción en el aula.", "3"),
        ("Se utilizan herramientas digitales como medio de comunicación interna y externa sobre actividades del programa STEM", "4"),
        ("Se establece uno o varios espacios de creación (Maker Spaces) para fomentar la creatividad y el desarrollo de proyectos", "5"),
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