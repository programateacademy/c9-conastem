from django.db import models
from ..GeneralModel import GeneralModel

class ConsideracionesAyA (GeneralModel):
    ITEM_CHOICE = [
        ("2.1.1","Formas innovadoras de enseñanza y aprendizaje en las áreas y asignaturas")
    ]

    numeral = models.CharField(
        max_length= 10000,
        choices= ITEM_CHOICE
    )

    SUB_NUMERAL_CHOICE =[
        ("2.1.1.1","Ciencias naturales: Nueva forma de la enseñanza de las ciencias, indagación, aprender haciendo, prácticas de ciencia e ingeniería, conceptos transversales como hábitos mentales desde los primeros años escolares."),
        ("2.1.1.2","Tecnología: Mayor intensidad horaria a la asignatura de tecnología. Se incluyen nuevos temas más amplios en la enseñanza de la tecnología. Se lideran proyectos interdisciplinarios asociados al currículo escolar."),
        ("2.1.1.3","Matemáticas: Las prácticas de matemáticas son fundamentales en la enseñanza y el aprendizaje, esta asignatura prima dentro de la gran mayoría de las actividades interdisciplinarias."),
        ("2.1.1.4","Ciencias Sociales: Hacen parte activa de la gran mayoría de los proyectos interdisciplinarios del Programa en Educación STEM, trabajan de forma directa con sus colegas en ciencias, matemáticas, así como con las demás asignaturas. Docentes conscientes de la importancia de su asignatura en los proyectos escolares.")
        ("2.1.1.5","Humanidades: Hacen parte activa de la gran mayoría de los proyectos interdisciplinarios del Programa en Educación STEM, trabajan de forma directa con sus colegas en ciencias, matemáticas, así como con las demás asignaturas. Docentes conscientes de la importancia de su asignatura en los proyectos escolares."),
        ("2.1.1.6","Educación Física: El área de educación Física incluye ahora conceptos de estadística, análisis de datos del desempeño de deportistas de diferentes especialidades, se traen temas de desarrollo tecnológico y científico en el deporte y el bienestar físico y mental de los estudiantes."),
        ("2.1.1.7","Educación Artística: Las artes plásticas, así como la música, participan de forma activa en los proyectos interdisciplinarios. Apoyan a sus colegas en la planeación y ejecución de actividades. Se destaca el desarrollo artístico del estudiante y se hace énfasis de la participación del arte dentro de las actividades humanas como técnicas, científicas y sociales."),
    ]
    
    def __str__(self) :
        return self.numeral