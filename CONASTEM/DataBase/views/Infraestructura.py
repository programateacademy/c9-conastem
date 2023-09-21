from django.http import HttpResponseRedirect
from ..forms import Form_Compromisodelacomunidad
from ..forms import Form_Convivenciaescolar
from ..forms import Form_Relacionesconlacomunidad
from ..forms import Form_Sostenibilidadescuela
from django.shortcuts import render
from django.views import generic
from django.utils import timezone

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
    context_object_name='Infraestructura'
    template_name='database\Infraestructura\Infraestructura.html'

class AmbienteEscolarListView(generic.ListView):
    model=AmbienteEscolar
    context_object_name='Ambiente_escolar_list'
    template_name='database\Infraestructura\Ambiente_escolar.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return AmbienteEscolar.objects.all().order_by('codigo')
    
# FORMULARIO
def Compromisodelacomunidad_new(request):
    if request.method == "POST":
        form_new = Form_Compromisodelacomunidad(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/compromisodelacomunidad')
    else:
        form_new = Form_Compromisodelacomunidad ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'Compromiso de la comunidad'})

    
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