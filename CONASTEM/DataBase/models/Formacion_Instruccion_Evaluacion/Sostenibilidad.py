from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class SostenibilidadFormacionInstruccion (GeneralModel):

    ITEM_CHOICE = [
        ('SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN', '3900'),
        ('A través del proceso de evaluación del programa en educación STEM se deberán hacer los cambios o actualizaciones a la instrucción para dar a los estudiantes oportunidades efectivas de aprendizaje.', '3910'),
        ('Se debe garantizar que los docentes incluyan nuevas actividades con nuevos contextos para los estudiantes. Nuevos contenidos y material curricular deben estar en constante desarrollo.', '3920'),
        ('Desarrollo de experiencias, eventos o competencias en educación STEM con otras instituciones mantienen vivo el espíritu creativo dentro de la comunidad educativa y promueve nuevos desarrollos novedosos por parte de docentes y estudiantes.', '3930'),
    ]

    numeral = models.CharField(max_length=240, choices=ITEM_CHOICE)

    class Meta: 
        verbose_name = ("Sostenibilidad - Formación/Instrucción/Evaluación")
        verbose_name_plural = ("Sostenibilidad - Formación/Instrucción/Evaluación")
    
    def __str__(self):
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("sostenibilidad_detail", args=[str(self.id)])