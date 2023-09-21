from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class TecnologiaFormacion(GeneralModel):

    ITEM_CHOICE = [
        ('3500', 'TECNOLOGÍA PARA LA FORMACIÓN / INSTRUCCIÓN'),
        ('3510', 'Los docentes utilizan elementos tecnológicos que apoyan la docencia de forma diaria.'),
        ('3520', 'Los profesores requieren que los estudiantes usen la tecnología apropiada y disponible para el trabajo de colaboración, comunicación, investigación,  recopilación y análisis de datos, en proyectos y otras evaluaciones diarias'),
        ('3530', 'Herramientas computacionales y tecnologías virtuales están integradas al Programa en Educación STEM.')
    ]

    numeral = models.CharField(
        max_length= 250,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
    )

    codigo = models.CharField(max_length=7, default='3000')
    def save(self, *args, **kwargs):
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break
        super(TecnologiaFormacion, self).save(*args, **kwargs)
    

    class Meta:
        verbose_name = ('Tecnología para la formacion / instrucción')
        verbose_name_plural = ('Tecnología para la formacion / instrucción')

    def __str__(self):
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("tecnologia_formacion_detail", args=[str(self.id)])