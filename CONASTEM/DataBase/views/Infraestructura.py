from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Infraestructura.ambiente_escolar import AmbienteEscolar
from ..models.Infraestructura.desarrollo_de_equipos_lideres import DesarrolloDeEquiposLideres
from ..models.Infraestructura.equidad import Equidad
from ..models.Infraestructura.planeacion_institucional import PlaneacionInstitucional
from ..models.Infraestructura.recursos_tecnologicos import RecursosTecnologicos
from ..models.Infraestructura.sostenibilidad import Sostenibilidad
from ..models.Infraestructura.uso_de_informacion import UsoDeInformacion

class InfraestructuraListView(generic.ListView):
    model=AmbienteEscolar
    context_object_name='AmbienteEscolar'
    template_name='database\Infraestructura\AmbienteEscolar.html'

class AmbienteEscolarListView(generic.ListView):
    model=AmbienteEscolar
    context_object_name='AmbienteEscolar'
    template_name='database\Infraestructura\AmbienteEscolar.html'
    
class DesarrolloDeEquiposLideresListView(generic.ListView):
    model=DesarrolloDeEquiposLideres
    context_object_name='DesarrolloDeEquiposLideres'
    template_name='database\Infraestructura\DesarrolloDeEquiposLideres.html'
    
class EquidadListView(generic.ListView):
    model=Equidad
    context_object_name='Equidad'
    template_name='database\Infraestructura\Equidad.html'
    
class PlaneacionInstitucionalListView(generic.ListView):
    model=PlaneacionInstitucional
    context_object_name='PlaneacionInstitucional'
    template_name='database\Infraestructura\PlaneacionInstitucional.html'

class RecursosTecnologicosListView(generic.ListView):
    model=RecursosTecnologicos
    context_object_name='RecursosTecnologicos'
    template_name='database\Infraestructura\RecursosTecnologicos.html'

class SostenibilidadListView(generic.ListView):
    model=Sostenibilidad
    context_object_name='Sostenibilidad'
    template_name='database\Infraestructura\Sostenibilidad.html'
    
class UsoDeInformacionListView(generic.ListView):
    model=UsoDeInformacion
    context_object_name='UsoDeInformacion'
    template_name='database\Infraestructura\UsoDeInformacion.html'