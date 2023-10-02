from django.db import models
from django.urls import reverse
from ..GeneralModel import GeneralModel

# 2.1 CONSIDERACIONES SOBRE LAS ÁREAS Y LAS ASIGNATURAS

class ConsideracionesSobreAreasYAsignaturas (GeneralModel):
    ITEM_CHOICE = [
        ("2000","CURRÍCULO"),
        ("2100","CONSIDERACIONES SOBRE LAS ÁREAS Y LAS ASIGNATURAS"),
        ("2110","Formas innovadoras de enseñanza y aprendizaje en las áreas y asignaturas"),
        ("2111","Ciencias naturales: Nueva forma de la enseñanza de las ciencias, indagación, aprender haciendo, prácticas de ciencia e ingeniería, conceptos transversales como hábitos mentales desde los primeros años escolares."),
        ("2112","Tecnología: Mayor intensidad horaria a la asignatura de tecnología. Se incluyen nuevos temas más amplios en la enseñanza de la tecnología. Se lideran proyectos interdisciplinarios asociados al currículo escolar."),
        ("2113","Matemáticas: Las prácticas de matemáticas son fundamentales en la enseñanza y el aprendizaje, esta asignatura prima dentro de la gran mayoría de las actividades interdisciplinarias."),
        ("2114","Ciencias Sociales: Hacen parte activa de la gran mayoría de los proyectos interdisciplinarios del Programa en Educación STEM, trabajan de forma directa con sus colegas en ciencias, matemáticas, así como con las demás asignaturas. Docentes conscientes de la importancia de su asignatura en los proyectos escolares."),
        ("2115","Humanidades: Hacen parte activa de la gran mayoría de los proyectos interdisciplinarios del Programa en Educación STEM, trabajan de forma directa con sus colegas en ciencias, matemáticas, así como con las demás asignaturas. Docentes conscientes de la importancia de su asignatura en los proyectos escolares."),
        ("2116","Educación Física: El área de educación Física incluye ahora conceptos de estadística, análisis de datos del desempeño de deportistas de diferentes especialidades, se traen temas de desarrollo tecnológico y científico en el deporte y el bienestar físico y mental de los estudiantes."),
        ("2117","Educación Artística: Las artes plásticas, así como la música, participan de forma activa en los proyectos interdisciplinarios. Apoyan a sus colegas en la planeación y ejecución de actividades. Se destaca el desarrollo artístico del estudiante y se hace énfasis de la participación del arte dentro de las actividades humanas como técnicas, científicas y sociales."),
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
                self.numeral = choice[1]
                break

        super(ConsideracionesSobreAreasYAsignaturas, self).save(*args, **kwargs)
    
    def __str__(self) :
        return self.numeral
    
    def get_absolute_url(self):
        return reverse("ConsideracionesSobreAreasYAsignaturas", kwargs={"pk": self.pk})
    