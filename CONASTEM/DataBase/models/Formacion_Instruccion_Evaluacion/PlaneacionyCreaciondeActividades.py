from django.db import models
from ..GeneralModel import GeneralModel


class PlaneacionyCreaciondeActividades (GeneralModel):

    ITEM_CHOICE = [
        ("3300","Planeación y creación de actividades"),
        ("3310","Las actividades planeadas y diseñadas incluyen métodos de indagación e investigación."),
        ("3320","Las actividades planeadas incluyen modelos explicativos y pensamiento crítico."),
        ("3330","Los estudiantes participarán en actividades que incluyen problemas auténticos del mundo real"),
        ("3331","Los estudiantes deben enfrentar problemas del mundo real, globales, de su país, región o ciudad, problemas que le son de su diario vivir."),
        ("3332","La educación STEM pone en contexto problemas de la vida que un ciudadano preparado debe poder enfrentar o que al menos participe en discusiones públicas donde aporte soluciones a la comunidad."),
        ("3340","Los profesores se reúnen regularmente para reflexionar sobre el trabajo de los estudiantes."),
        ("3350","La institución mantiene docentes que capacitan otros docentes en el ámbito de lo formativo y pedagógico")
        ]

    numeral = models.CharField(
        max_length= 10000,
        choices=[(choice[0], f"{choice[0]} - {choice[1]}") for choice in ITEM_CHOICE]
        )
    codigo =models.CharField(max_length=4)
    def save(self, *args, **kwargs):
        # Buscar el número correspondiente al ítem seleccionado en ITEM_CHOICE
        for choice in self.ITEM_CHOICE:
            if choice[0] == self.numeral:
                self.codigo = choice[0]
                self.numeral = choice[1]
                break

        super(PlaneacionyCreaciondeActividades, self).save(*args, **kwargs)

    def __str__(self) :
        return self.numeral