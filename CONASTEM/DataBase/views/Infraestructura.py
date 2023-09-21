from django.http import HttpResponseRedirect
from ..forms import AmbienteEscolarForm
from ..forms import DesarrolloEquiposLideresForm
from ..forms import EquidadForm
from ..forms import PlaneacionInstitucionalForm
from ..forms import RecursosTecnologicosForm
from ..forms import SostenibilidadForm
from ..forms import UsoDeInfoForm
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
def Ambiente_escolar_new(request):
    if request.method == "POST":
        form_new = AmbienteEscolarForm(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/ambiente-escolar')
    else:
        form_new = AmbienteEscolarForm ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'1300-AMBIENTE ESCOLAR'})

class DesarrolloDeEquiposLideresListView(generic.ListView):
    model=DesarrolloDeEquiposLideres
    context_object_name='Desarrollo_de_equipos_lideres_list'
    template_name='database\Infraestructura\Desarrollo_de_equipos_lideres.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return DesarrolloDeEquiposLideres.objects.all().order_by('codigo')

def desarrollo_de_equipos_lideres_new(request):
    if request.method == "POST":
        form_new = DesarrolloEquiposLideresForm(request.POST) 
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/desarrollo-equipos-lideres')
    else:
        form_new = DesarrolloEquiposLideresForm ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new , 'titulo':'1100-DESARROLLO DE EQUIPOS LIDERES'})
 
class EquidadListView(generic.ListView):
    model=Equidad
    context_object_name='Equidad_list'
    template_name='database/Infraestructura/Equidad.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return Equidad.objects.all().order_by('codigo')

def Equidad_new(request):
    if request.method == "POST":
        form_new = EquidadForm(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/equidad')
    else:
        form_new = EquidadForm ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new , 'titulo':'1600-EQUIDAD'})
    
class PlaneacionInstitucionalListView(generic.ListView):
    model=PlaneacionInstitucional
    context_object_name='Planeacion_institucional_list'
    template_name='database/Infraestructura/Planeacion_institucional.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return PlaneacionInstitucional.objects.all().order_by('codigo')

def Planeacion_institucional_new(request):
    if request.method == "POST":
        form_new = PlaneacionInstitucionalForm(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/planeacion_institucional')
    else:
        form_new = PlaneacionInstitucionalForm ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new , 'titulo':'1200-PLANEACIÓN INSTITUCIONAL'})

class RecursosTecnologicosListView(generic.ListView):
    model=RecursosTecnologicos
    context_object_name='Recursos_tecnologicos_list'
    template_name='database/Infraestructura/Recursos_tecnologicos.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return RecursosTecnologicos.objects.all().order_by('codigo')

def Recursos_tecnologicos_new(request):
    if request.method == "POST":
        form_new = RecursosTecnologicosForm(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/Recursos-tecnologicos')
    else:
        form_new = RecursosTecnologicosForm ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new , 'titulo':'1400-RECURSOS TECNOLÓGICOS'})

class SostenibilidadListView(generic.ListView):
    model=Sostenibilidad
    context_object_name='Sostenibilidad_list'
    template_name='database/Infraestructura/Sostenibilidad.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return Sostenibilidad.objects.all().order_by('codigo')

def Sostenibilidad_new(request):
    if request.method == "POST":
        form_new = SostenibilidadForm(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/sostenibilidad')
    else:
        form_new = SostenibilidadForm ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new , 'titulo':'1700-SOSTENIBILIDAD - INFRAESTRUCTURA'})
    
class UsoDeInformacionListView(generic.ListView):
    model=UsoDeInformacion
    context_object_name='Uso_informacion_list'
    template_name='database/Infraestructura/Uso_informacion.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return UsoDeInformacion.objects.all().order_by('codigo')

def Uso_de_info_new(request):
    if request.method == "POST":
        form_new = UsoDeInfoForm(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/uso-de-info')
    else:
        form_new = UsoDeInfoForm ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new , 'titulo':'1500-USO DE LA INFORMACIÓN (DATOS)'})