from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

class EleccionCarrera (GeneralModel):

    ITEM_CHOICE = [
        ('ELECCIÓN DE CARRERA', '3700'),
        ('La institución educativa programa y promueve actividades Universitarias tempranas.', '3710'),
        ('Los estudiantes participan en actividades universitarias tempranas, tales como cursos universitarios.', '3711'),
        ('Los estudiantes participan en clases universitarias desde los últimos grados de formación escolar.', '3712'),
        ('Dentro de la planeación de la institución educativa se tienen previsto establecer alianzas con universidades.', '3720'),
        ('Programar actividades de promoción de carreras de las universidades en el campus del colegio.', '3721'),
        ('Programar eventos universitarios donde los estudiantes visiten las universidades y conozcan las opciones que ofrecen.', '3722'),
        ('Establecer y programar cursos universitarios para estudiantes de  los últimos grados, tales como cálculos, físicas, químicas, termodinámica, cursos de herramientas computacionales para diseño y representación gráfica, cursos de impresión 3D, etc.', '3723'),
        ('Hacer uso del conocimiento de profesionales en universidades para el desarrollo de proyectos académicos de los estudiantes.', '3724'),
        ('Dentro de la planeación de la institución educativa se tiene previsto establecer alianzas con la industria y la empresa privada', '3730'),
        ('Establecer y programar visitas de empresas al colegio con el objetivo de mostrar sus productos y procesos a los estudiantes.', '3731'),
        ('Establecer y programar visitas guiadas de los estudiantes a empresas para conocer de primera mano productos y procesos.', '3732'),
        ('Hacer uso del conocimiento de profesionales en la empresa privada para el desarrollo de proyectos académicos de los estudiantes.', '3733'),
        ('Programar charlas y presentaciones de profesionales de las diferentes áreas STEM con el objetivo de mostrarle a los estudiantes su campo de desempeño y los nuevos campos de acción en carreras similares o nuevas.', '3734'),
        ('Dentro de la planeación de la institución educativa se tiene previsto establecer alianzas con institutos de desarrollo técnico.', '3740'),
        ('Programar actividades de promoción de carreras de las universidades en el campus del colegio.', '3741'),
        ('Establecer y programar cursos técnicos para estudiantes de  los últimos grados en áreas de desempeño innovadoras y que estén gestando nuevas áreas de trabajo.', '3742'),
        ('Hacer uso del conocimiento de profesionales en institutos técnicos para el desarrollo de proyectos académicos de los estudiantes', '3743'),
        ('El emprendimiento es parte fundamental de las nuevas oportunidades laborales y del futuro de los estudiantes. La institución tiene un programa de emprendimiento asociado al Programa en Educación STEM.', '3750'),
        ('Las experiencias con expertos externos, así como las experiencias de orden universitario se incluyen dentro del diseño de actividades en educación STEM y no se limita a la educación media.', '3760'),
    ]

<<<<<<< HEAD
    numeral = models.CharField (max_length=300, choices=ITEM_CHOICE)
=======
    numeral = models.CharField (max_length=500, choices=ITEM_CHOICE)
>>>>>>> f1b5f97d5b1695193a01adf1350fc6d82a760b27

    class Meta:
        verbose_name = ('Elección de carrera')
        verbose_name_plural = ('Elección de carrera')

    def __str__(self):
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("eleccion_carrera_detail", args=[str(self.id)])