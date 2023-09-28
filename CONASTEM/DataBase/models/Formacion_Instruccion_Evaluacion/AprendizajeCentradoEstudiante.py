from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 3.1 APRENDIZAJE CENTRADO EN EL ESTUDIANTE

class AprendizajeCentrado (GeneralModel):

    ITEM_CHOICE = [
        ('3000', 'FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN'),
        ('3100', 'APRENDIZAJE CENTRADO EN EL ESTUDIANTE'),
        ("3110", "Formación/Instrucción basada en Aprendizaje Basado en Lecciones / Aprendizaje Basado en Proyectos / Aprendizaje enfocado en la indagación."),
        ("3120", "El aprendizaje es centrado en el estudiante. La dinámica de aula y en general en la institución se prevé el tiempo para investigación y trabajo en equipo, así como de tiempo de consulta a los profesores en tiempo fuera del horario de la asignatura."),
        ("3121", "Autonomía del estudiante"),
        ("3122", "Los estudiantes descubren qué lo que están aprendiendo es importante para su vida y su comunidad."),
        ("3123", "Los estudiantes le dan importancia y relevancia a las actividades que se hacen durante sus clases. Toman control sobre el desarrollo del aprendizaje."),
        ("3124", "Los estudiantes demuestran su conocimiento sobre las áreas STEM y que son base de una formación en educación STEM"),
        ("3130", "Los proyectos son centrales al currículo. Los objetivos de los proyectos serán la meta más importante para lograr aprobar el grado escolar."),
        ("3140", "Dentro de las experiencias de aula predominarán los retos de ingeniería como parte del ABP-ABL."),
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    
    codigo = models.CharField(max_length=7, default='3000')
    def save(self, *args, **kwargs):
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break
        super(AprendizajeCentrado, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = ("Aprendizaje centrado en el estudiante")
        verbose_name_plural = ("Aprendizaje centrado en el estudiante")

    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("aprendizaje_centrado_detail", kwargs={"pk": self.pk})
    