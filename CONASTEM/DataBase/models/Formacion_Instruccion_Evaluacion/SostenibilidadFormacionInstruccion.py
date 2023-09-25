from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class SostenibilidadFormacionInstruccion (GeneralModel):

    ITEM_CHOICE = [
        ('3900', 'SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN'),
        ('3910', 'A través del proceso de evaluación del programa en educación STEM se deberán hacer los cambios o actualizaciones a la instrucción para dar a los estudiantes oportunidades efectivas de aprendizaje.'),
        ('3920', 'Se debe garantizar que los docentes incluyan nuevas actividades con nuevos contextos para los estudiantes. Nuevos contenidos y material curricular deben estar en constante desarrollo.'),
        ('3930', 'Desarrollo de experiencias, eventos o competencias en educación STEM con otras instituciones mantienen vivo el espíritu creativo dentro de la comunidad educativa y promueve nuevos desarrollos novedosos por parte de docentes y estudiantes.'),
    ]

    numeral = models.CharField(
        max_length=240, 
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo = models.CharField(max_length=7, default='3000')
    def save(self, *args, **kwargs):
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break
        super(SostenibilidadFormacionInstruccion, self).save(*args, **kwargs)
    

    class Meta: 
        verbose_name = ("Sostenibilidad - Formación/Instrucción/Evaluación")
        verbose_name_plural = ("Sostenibilidad - Formación/Instrucción/Evaluación")
    
    def __str__(self):
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("sostenibilidad_detail", args=[str(self.id)])