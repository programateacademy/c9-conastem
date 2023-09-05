from django.db import models
from django.db.models import Case, Value, When
from ..Person_Responsable import PersonResponsable
from ..Auditory import Auditory
from ..Criterio import Criterio

# 1.5 Equidad
class Equidad(models.Model):

    criterio = models.ForeignKey (Criterio, null= True, on_delete=models.SET_NULL, default= "INFRAESTRUCTURA")

    # sub_criterio = models.CharField ()

    ITEM_CHOICE = (
        (1 ,"Todos los estudiantes reciben acceso equitativo a la formación y a los programas. No se selecciona únicamente a los estudiantes con gusto por las asignaturas S.T.E.M., todos los estudiantes hacen parte del programa"),
        (2, "Todos los estudiantes con necesidades específicas e identificadas están siendo ubicados para facilitar su adaptación. Aprendizaje individualizado."),
        (3, "Se han diseñado acciones o planes especiales para alentar a los estudiantes con bajo interés o desempeño a desarrollar interés en las carreras STEM."),
        (4, "Los docentes reciben desarrollo profesional sobre las diferencias culturales y de género para enriquecer la formación."),
        (5, "El aula STEM se diferencia en ubicar a todos los estudiantes, con una consideración especial hacia todos los grupos geográficos, socioeconómicos, raciales, étnicos y de género."),
        (6, "La institución está preparada para proveer una formación incluyente. Promueve las oportunidades de aprendizaje para todos los estudiantes, pero respeta las diferencias culturales y de género."),
    )

    item = models.CharField (max_length=6, primary_key= True, choices= ITEM_CHOICE)

    SUB_ITEM_CHOICE = (
        (1, "Procesos claros desarrollados para la inducción de nuevos estudiantes."),
        (2, "Programa o actividades que garanticen una transición efectiva para los estudiantes."),
        (3, "La educación STEM es incluyente, y una forma importante es hacer que se sientan como en casa a través de actividades o de programas, con suficiente anterioridad para que puedan participar en la labor académica, no como extraños sino ya apropiados de las costumbres de los estudiantes veteranos."),
        (4, "La institución tiene por objetivo incrementar la participación de la mujer en las áreas STEM, de tal manera que la población estudiantil involucrada en el programa sea cada vez mayor. "),
    )

    # sub_item = Case (
    #     When(numeral.primary_key == 6, then= (SUB_ITEM_CHOICE))
    # )

    PRIORITY_MODEL_CHOICE = (
        (1, "Exploratorio"),
        (2, "Introductorio"),
        (3, "Inmerción parcial"),
        (4, "Inmerción completa"),
    )

    priority_model = models.CharField (max_length=4, choices= PRIORITY_MODEL_CHOICE, default= "Introductorio")
    
    dep_responsable = models.CharField (max_length=30, default= "Dirección")
    
    person_responsable = models.ManyToManyField(PersonResponsable, help_text= "Seleccione un responsable")
    
    track_year = models.IntegerField (help_text="Ingrese año de seguimiento")
    
    track_date = models.CharField(max_length=5, help_text="Ingrese fecha de seguimiento")
    
    auditory = models.ForeignKey(Auditory, null= True, on_delete=models.SET_NULL)