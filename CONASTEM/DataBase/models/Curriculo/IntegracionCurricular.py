from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.4 INTEGRACIÓN CURRICULAR

class IntegracionCurricular(GeneralModel):

    ITEM_CHOICE = [
        ("2400", "INTEGRACIÓN CURRICULAR"),
        ("2410", "Las unidades de formación del tipo  Aprendizaje Basado en Proyectos ABP / Investigación incluyen educación STEM integrada a las ciencias y las matemáticas y con todas las áreas del currículo, durante los cuatro trimestres del año académico."),
        ("2420", "Desarrollo de actividades interdisciplinarias que promueven la relevancia de los temas y se conectan con problemas del mundo real."),
        ("2430", "La selección de termas para las actividades no solamente sale del plan curricular sino de la realimentación que brindan los estudiantes con respecto a los asuntos que más les interesan de su vida diaria"),
        ("2440", "Se ofrecen clases interdisciplinarias donde los profesores enseñan conjuntamente unidades académicas."),
        ("2450", "La integración curricular se hace con todas las asignaturas del currículo. Cada diseño de actividad integra intencionalmente varias asignaturas en torno a los objetivos de aprendizaje."),
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
            
        super(IntegracionCurricular, self).save(*args, **kwargs)
    
    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("IntegracionCurricular", kwargs={"pk": self.pk})
    