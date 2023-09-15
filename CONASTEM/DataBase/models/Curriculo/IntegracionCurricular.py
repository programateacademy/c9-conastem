from datetime import timezone
from django.db import models
from django.urls import reverse

from ..Person_Responsable import PersonResponsable
from ..GeneralModel import GeneralModel

# 2.4 Integración curricular
class Inclusioncurricular(GeneralModel):

    ITEM_CHOICE = [
        ("2.4.1", "Las unidades de formación del tipo  Aprendizaje Basado en Proyectos ABP / Investigación incluyen educación STEM integrada a las ciencias y las matemáticas y con todas las áreas del currículo, durante los cuatro trimestres del año académico."),
        ("2.4.2", "Desarrollo de actividades interdisciplinarias que promueven la relevancia de los temas y se conectan con problemas del mundo real."),
        ("2.4.3", "La selección de termas para las actividades no solamente sale del plan curricular sino de la realimentación que brindan los estudiantes con respecto a los asuntos que más les interesan de su vida diaria"),
        ("2.4.4", "Se ofrecen clases interdisciplinarias donde los profesores enseñan conjuntamente unidades académicas."),
        ("2.4.5", "La integración curricular se hace con todas las asignaturas del currículo. Cada diseño de actividad integra intencionalmente varias asignaturas en torno a los objetivos de aprendizaje."),
    ]

    person_responsable = models.ManyToManyField(PersonResponsable, help_text="Seleccione un responsable", default=None)

    numeral = models.CharField(
        max_length=1000, 
        choices=ITEM_CHOICE
    )

    def __str__(self):
        return self.numeral

    def get_absolute_url(self):
        return reverse("IntegracionCurricular", args=[str(self.id)])
