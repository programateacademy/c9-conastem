from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Curriculo.Inclusion_ingenieria_aula import InclusionIngenieriaAula
from ..models.Curriculo.Desarrollo_ciudadania_digital import DesarrolloCiudadaniaDigital
from ..models.Curriculo.Curriculo_progresivo import CurriculoProgresivo
from ..models.Curriculo.Curriculo_propio import CurriculoPropio
from ..models.Curriculo.Evaluacion_estudiantes import EvaluacionEstudiantes

# 2.1 CONSIDERACIONES SOBRE LAS ÁREAS Y LAS ASIGNATURAS

# 2.2 Inclusion ingenieria aula
class InclusionIngenieriaAulaListView(generic.ListView):
    model = InclusionIngenieriaAula
    context_object_name = 'Inclusion_ingenieria_aula_list'
    template_name = 'database/Curriculo/Inclusion_ingenieria_aula_list.html'

# 2.3 Desarrollo ciudadania digital
class DesarrolloCiudadaniaDigitalListView(generic.ListView):
    model = DesarrolloCiudadaniaDigital
    context_object_name = 'Desarrollo_ciudadania_digital_list'
    template_name = 'database/Curriculo/Desarrollo_ciudadania_digital_list.html'

# 2.4 INTEGRACIÓN CURRICULAR

# 2.5 CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES
class CurriculoProgresivoListView(generic.ListView):
    model = CurriculoProgresivo
    context_object_name = 'Curriculo_progresivo_list'
    template_name = 'database/Curriculo/Curriculo_progresivo_list.html'

# 2.6 CURRÍCULO PROPIO
class CurriculoPropioListView(generic.ListView):
    model = CurriculoPropio
    context_object_name = 'Curriculo_propio_list'
    template_name = 'database/Curriculo/Curriculo_propio_list.html'

# 2.7 DESARROLLO DE LAS HABILIDADES DEL SIGLO XXI

# 2.8 EVALUACIÓN DE LOS ESTUDIANTES
class EvaluacionEstudiantesListView(generic.ListView):
    model = EvaluacionEstudiantes
    context_object_name = 'Evaluacion_estudiantes_list'
    template_name = 'database/Curriculo/Evaluacion_estudiantes_list.html'