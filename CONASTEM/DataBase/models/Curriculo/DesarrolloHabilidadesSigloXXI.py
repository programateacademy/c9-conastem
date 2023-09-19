from datetime import timezone
from django.db import models
from django.urls import reverse

from ..Person_Responsable import PersonResponsable
from ..GeneralModel import GeneralModel

# 2.7 Desarrollo de las habilidadees del siglo XXI
class DesarroloHabilidadesSigloXXI(GeneralModel):

    ITEM_CHOICE = [
        ("2.7.1", "Se ha incluido la ingeniería como parte del currículo escolar para el desarrollo efectivo de las habilidades de pensamiento crítico, solución de problemas, pensamiento computacional y pensamiento matemático"),
        ("2.7.2", "Se ha incluido estrategias como el Aprendizaje Basado en Proyectos y enfoque en la investigación/indagación para promover el trabajo en equipo y desarrollar habilidades y competencias del trabajo colaborativo."),
        ("2.7.3", "La dinámica de aula permite el desarrollo de habilidades de investigación e indagación. Promueve la curiosidad y facilita medios de acceso a la información, así como el apoyo de forma importante del docente o equipos de docentes."),
        ("2.7.4", "Se ha incluido la ingeniería en el aula y el aporte interdisciplinario del área de Artes para promover la creatividad complementada desde lo estético en los estudiantes"),
        ("2.7.5", "Las áreas de ciencias sociales se integran de forma interdisciplinaria para dar sentido a lo que se aprende."),
        ("2.7.6", "Se ha incluido el área de humanidades con el objetivo de desarrollar habilidades comunicativas del estudiante a través de métodos tradicionales y métodos innovadores"),
    ]

    person_responsable = models.ManyToManyField(PersonResponsable, help_text="Seleccione un responsable", default=None)

    numeral = models.CharField(
        max_length=1000, 
        choices=ITEM_CHOICE
    )

    def __str__(self):
        return self.numeral

    def get_absolute_url(self):
        return reverse("DesarroloHabilidadesSigloXXI", args=[str(self.id)])
