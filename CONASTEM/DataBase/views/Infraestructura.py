from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Infraestructura.ambiente_escolar import AmbienteEscolar
from ..models.Infraestructura.desarrollo_de_equipos_lideres import DesarrolloDeEquiposLideres
from ..models.Infraestructura.Equidad import Equidad
from ..models.Infraestructura.planeacion_institucional import PlaneacionInstitucional
from ..models.Infraestructura.recursos_tecnologicos import RecursosTecnologicos
from ..models.Infraestructura.sostenibilidad import Sostenibilidad
from ..models.Infraestructura.uso_de_informacion import UsoDeInformacion

class InfraestructuraListView(generic.ListView):
    model=AmbienteEscolar
    context_object_name='Infraestructura'
    template_name='database\Infraestructura\Infraestructura.html'

class AmbienteEscolarListView(generic.ListView):
    model=AmbienteEscolar
    context_object_name='Ambiente_escolar_list'
    template_name='database\Infraestructura\Ambiente_escolar.html'
    
class DesarrolloDeEquiposLideresListView(generic.ListView):
    model=DesarrolloDeEquiposLideres
    context_object_name='Desarrollo_de_equipos_lideres_list'
    template_name='database\Infraestructura\Desarrollo_de_equipos_lideres.html'
    
class EquidadListView(generic.ListView):
    model=Equidad
    context_object_name='Equidad_list'
    template_name='database/Infraestructura/Equidad.html'
    
class PlaneacionInstitucionalListView(generic.ListView):
    model=PlaneacionInstitucional
    context_object_name='Planeacion_institucional_list'
    template_name='database/Infraestructura/Planeacion_institucional.html'

class RecursosTecnologicosListView(generic.ListView):
    model=RecursosTecnologicos
    context_object_name='Recursos_tecnologicos_list'
    template_name='database/Infraestructura/Recursos_tecnologicos.html'

class SostenibilidadListView(generic.ListView):
    model=Sostenibilidad
    context_object_name='Sostenibilidad_list'
    template_name='database/Infraestructura/Sostenibilidad.html'
    
class UsoDeInformacionListView(generic.ListView):
    model=UsoDeInformacion
    context_object_name='Uso_informacion_list'
    template_name='database/Infraestructura/Uso_informacion.html'