from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class TecnologiaFormacion(GeneralModel):

    ITEM_CHOICE = [
        ('Los docentes utilizan elementos tecnológicos que apoyan la docencia de forma diaria.', '3510'),
        ('Los profesores requieren que los estudiantes usen la tecnología apropiada y disponible para el trabajo de colaboración, comunicación, investigación,  recopilación y análisis de datos, en proyectos y otras evaluaciones diarias', '3520'),
        ('Herramientas computacionales y tecnologías virtuales están integradas al Programa en Educación STEM.', '3530')
    ]

    numeral = models.CharField(
        max_length= 250,
        choices= ITEM_CHOICE
    )

    class Meta:
        verbose_name = ('Tecnología para la formacion / instrucción')
        verbose_name_plural = ('Tecnología para la formacion / instrucción')

    def __str__(self):
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("tecnologia_formacion_detail", args=[str(self.id)])