from django.db import models
from ..GeneralModel import GeneralModel


class PlaneacionyCreaciondeActividades (GeneralModel):

    ITEM_CHOICE = [
        ("Planeación y creación de actividades","3300"),
        ("Las actividades planeadas y diseñadas incluyen métodos de indagación e investigación.","3310"),
        ("Las actividades planeadas incluyen modelos explicativos y pensamiento crítico.","3320"),
        ("Los estudiantes participarán en actividades que incluyen problemas auténticos del mundo real","3330"),
        ("Los estudiantes deben enfrentar problemas del mundo real, globales, de su país, región o ciudad, problemas que le son de su diario vivir.","3331"),
        ("La educación STEM pone en contexto problemas de la vida que un ciudadano preparado debe poder enfrentar o que al menos participe en discusiones públicas donde aporte soluciones a la comunidad.","3332"),
        ("Los profesores se reúnen regularmente para reflexionar sobre el trabajo de los estudiantes.","3340"),
        ("La institución mantiene docentes que capacitan otros docentes en el ámbito de lo formativo y pedagógico","3350")
        ]

	

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    codigo =models.CharField(max_length=7, default="3300")
    def __str__(self) :
        return self.numeral