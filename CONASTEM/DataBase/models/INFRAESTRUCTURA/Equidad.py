from django.db import models
from django.db.models import Case, Value, When
from ..Person_Responsable import PersonResponsable
from ..Auditory import Auditory

# 1.5 Equidad
class Equidad(models.Model):

    NUMERAL_CHOICE = (
        ("Todos los estudiantes reciben acceso equitativo a la formación y a los programas. No se selecciona únicamente a los estudiantes con gusto por las asignaturas S.T.E.M., todos los estudiantes hacen parte del programa"),
        ("Todos los estudiantes con necesidades específicas e identificadas están siendo ubicados para facilitar su adaptación. Aprendizaje individualizado."),
        ("Se han diseñado acciones o planes especiales para alentar a los estudiantes con bajo interés o desempeño a desarrollar interés en las carreras STEM."),
        ("Los docentes reciben desarrollo profesional sobre las diferencias culturales y de género para enriquecer la formación."),
        ("El aula STEM se diferencia en ubicar a todos los estudiantes, con una consideración especial hacia todos los grupos geográficos, socioeconómicos, raciales, étnicos y de género."),
        ("La institución está preparada para proveer una formación incluyente. Promueve las oportunidades de aprendizaje para todos los estudiantes, pero respeta las diferencias culturales y de género."),
    )

    numeral = models.CharField (primary_key= True)

    SUB_NUMERAL_CHOICE = (
        ("Procesos claros desarrollados para la inducción de nuevos estudiantes."),
        ("Programa o actividades que garanticen una transición efectiva para los estudiantes."),
        ("La educación STEM es incluyente, y una forma importante es hacer que se sientan como en casa a través de actividades o de programas, con suficiente anterioridad para que puedan participar en la labor académica, no como extraños sino ya apropiados de las costumbres de los estudiantes veteranos."),
        ("La institución tiene por objetivo incrementar la participación de la mujer en las áreas STEM, de tal manera que la población estudiantil involucrada en el programa sea cada vez mayor. "),
    )

    sub_numeral = Case (
        When(numeral == 6, then= (SUB_NUMERAL_CHOICE))
    )

    PRIORITY_MODEL_CHOICE = (
        ("Exploratorio"),
        ("Introductorio"),
        ("Inmerción parcial"),
        ("Inmerción completa"),
    )

    priority_model = models.CharField (choices= PRIORITY_MODEL_CHOICE, default= "Introductorio")
    
    dep_responsable = models.CharField (default= "Dirección")
    
    person_responsable = models.ManyToManyField(PersonResponsable, help_text= "Seleccione un responsable")
    
    track_year = models.IntegerField (help_text="Ingrese año de seguimiento")
    
    track_date = models.CharField(max_length=5, help_text="Ingrese fecha de seguimiento")
    
    auditory = models.ForeignKey(Auditory, null= True, on_delete=models.SET_NULL)