from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.7 Desarrollo de las habilidadees del siglo XXI
class DesarrolloHabilidadesSigloXXI(GeneralModel):

    ITEM_CHOICE = [
        ("2700", "DESARROLLO DE LAS HABILIDADES DEL SIGLO XXI"),
        ("2710", "Se ha incluido la ingeniería como parte del currículo escolar para el desarrollo efectivo de las habilidades de pensamiento crítico, solución de problemas, pensamiento computacional y pensamiento matemático"),
        ("2720", "Se ha incluido estrategias como el Aprendizaje Basado en Proyectos y enfoque en la investigación/indagación para promover el trabajo en equipo y desarrollar habilidades y competencias del trabajo colaborativo."),
        ("2730", "La dinámica de aula permite el desarrollo de habilidades de investigación e indagación. Promueve la curiosidad y facilita medios de acceso a la información, así como el apoyo de forma importante del docente o equipos de docentes."),
        ("2740", "Se ha incluido la ingeniería en el aula y el aporte interdisciplinario del área de Artes para promover la creatividad complementada desde lo estético en los estudiantes"),
        ("2750", "Las áreas de ciencias sociales se integran de forma interdisciplinaria para dar sentido a lo que se aprende."),
        ("2760", "Se ha incluido el área de humanidades con el objetivo de desarrollar habilidades comunicativas del estudiante a través de métodos tradicionales y métodos innovadores"),
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo = models.CharField(max_length=7, default='4000')
    def save(self, *args, **kwargs):
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break
            
        super(DesarrolloHabilidadesSigloXXI, self).save(*args, **kwargs)
    
    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("DesarrolloHabilidadesSigloXXI", kwargs={"pk": self.pk})
    