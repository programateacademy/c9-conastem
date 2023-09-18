from django.db import models
from ..GeneralModel import GeneralModel


class AprendizajeExtendido (GeneralModel):

    ITEM_CHOICE = [
        ("Aprendizaje extendido","3800"),
		("Las experiencias STEM están directamente conectadas con el aprendizaje en clase.","3810"),
		("El aprendizaje extendido incluye experiencias de campo y aprendizaje auténtico y contextual.","3823"),
		("Existen oportunidades para que los estudiantes mayores participen en pasantías después de la jornada de estudio o los fines de semana.","3830"),
		("El programa está asociado a algún parque de ciencia o museo","3840"),
		("El aprendizaje extendido está alineado con los estándares básicos de competencias en lenguaje, matemáticas, ciencias y competencias ciudadanas.","3850"),
		("Se utilizan guías para programas de formación extracurricular","3860"),
		("El programa extracurricular realiza sus propias evaluaciones y observaciones para garantizar la calidad de la experiencia STEM","3870"),
		("El programa extracurricular utiliza herramientas de observación basadas en la investigación alineadas con los estándares de experiencia STEM.","3880"),
		("Los estudiantes tienen experiencias directas con profesionales de STEM en entornos auténticos fuera del día escolar","3890"),
		("El trabajo de los alumnos se exhibe y se muestra a la comunidad y en el sitio web de la institución.","38100"),
	    ("Los estudiantes deben poder tener la oportunidad de involucrarse en actividades adicionales de todo tipo, culturales, deportes, artísticas y también en actividades en educación STEM que los exponga a otros contextos para que puedan tener una perspectiva más amplia de la vida y de las oportunidades que se ofrecen. De esta forma tendremos más oportunidades para un aprendizaje holístico.","38110"),
    ]
    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
        )
    codigo =models.CharField(max_length=7, default="3800")
    
    def __str__(self):
        return self.numeral