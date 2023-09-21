from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.9 SOSTENBILIDAD - CURRÍCULO
class SostenibilidadCurriculo(GeneralModel):

    ITEM_CHOICE = [
        ("2900", "SOSTENIBILIDAD - CURRÍCULO"),
        ("2910", "Mantener el currículo acorde a las necesidades del campo laboral futuro de los estudiantes y hacer los cambios necesarios para su correcta adaptación."),
        ("2920", "A través del proceso de evaluación del Programa en Educación STEM se deberá hacer los cambios o actualizaciones al currículo para dar a los estudiantes aporte efectivo en su aprendizaje en educación STEM."),
        ("2930", "La organización de la institución educativa incluye dentro de su organización un especialista en currículo. Para ello debe estar nominado y operando activamente dentro del Programa en Educación STEM."),
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
                break
        super(SostenibilidadCurriculo, self).save(*args, **kwargs)
    
    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("SostenibilidadCurriculo", kwargs={"pk": self.pk})
    