from django.db import models
from django.urls import reverse
from .Criterio import Criterio


class SubCriterio (models.Model):

    SUB_CRITERIO_CHOICE = [
        ("DESARROLLO DE EQUIPOS LÍDERES", "1.1"),
        ("PLANEACIÓN INSTITUCIONAL", "1.2"),
        ("AMBIENTE ESCOLAR", "1.3"),
        ("RECURSOS TECNOLÓGICOS", "1.4"),
        ("USO DE LA INFORMACIÓN (DATOS)", "1.5"),
        ("EQUIDAD", "1.6"),
        ("SOSTENIBILIDAD - INFRAESTRUCTURA", "1.7"),
        ("CONSIDERACIONES SOBRE LAS ÁREAS Y LAS ASIGNATURAS", "2.1"),
        ("INCLUSIÓN DE LA INGENIERÍA EN EL AULA", "2.2"),
        ("DESARROLLO DE UNA CIUDADANÍA DIGITAL", "2.3"),
        ("INTEGRACIÓN CURRICULAR", "2.4"),
        ("CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES", "2.5"),
        ("CURRÍCULO PROPIO", "2.6"),
        ("DESARROLLO DE LAS HABILIDADES DEL SIGLO XXI", "2.7"),
        ("EVALUACIÓN DE LOS ESTUDIANTES", "2.8"),
        ("SOSTENIBILIDAD - CURRÍCULO", "2.9"),
        ("APRENDIZAJE CENTRADO EN EL ESTUDIANTE", "3.1"),
        ("APRENDIZAJE RIGUROSO", "3.2"),
        ("PLANEACIÓN Y CREACIÓN DE ACTIVIDADES", "3.3"),
        ("EDUCACIÓN STEM INTEGRADA", "3.4"),
        ("TECNOLOGÍA PARA LA FORMACIÓN / INSTRUCCIÓN", "3.5"),
        ("ESTRATEGIAS FORMATIVAS", "3.6"),
        ("ELECCIÓN DE CARRERA", "3.7"),
        ("APRENDIZAJE EXTENDIDO", "3.8"),
        ("SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN", "3.9"),
        ("PROFESIONALES ALTAMENTE CALIFICADOS ESPECIALIZADOS EN EDUCACIÓN STEM", "4.1"),
        ("DESARROLLO PROFESIONAL INICIAL Y CONTINUO PARA DOCENTES, DIRECTORES DE ESCUELA Y CONSEJEROS PROFESIONALES", "4.2"),
        ("APOYO PEDAGÓGICO PARA EL PERSONAL", "4.3"),
        ("SOSTENIBILIDAD - PERSONAL DOCENTE Y ADMINISTRATIVO", "4.4"),
        ("COMPROMISO DE LA COMUNIDAD", "5.1"),
        ("RELACIONES CON LA COMUNIDAD", "5.2"),
        ("CONVIVENCIA ESCOLAR", "5.3"),
        ("SOSTENIBILIDAD - ESCUELA, COMUNIDAD Y PERTENENCIA", "5.4")
    ]

    subcriterio = models.CharField(max_length=100, choices= SUB_CRITERIO_CHOICE)

    criterio = models.ForeignKey(Criterio, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = ("Sub criterio")
        verbose_name_plural = ("Sub criterios")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("subcriterios_detail", kwargs={"pk": self.pk})
