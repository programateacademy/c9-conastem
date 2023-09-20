from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Curriculo.ConsideracionesSobreAreasYAsignaturas import ConsideracionesSobreAreasYAsignaturas
from ..models.Curriculo.Inclusion_ingenieria_aula import InclusionIngenieriaAula
from ..models.Curriculo.Desarrollo_ciudadania_digital import DesarrolloCiudadaniaDigital
from ..models.Curriculo.IntegracionCurricular import Integracioncurricular
from ..models.Curriculo.Curriculo_progresivo import CurriculoProgresivo
from ..models.Curriculo.Curriculo_propio import CurriculoPropio
from ..models.Curriculo.DesarrolloHabilidadesSigloXXI import DesarroloHabilidadesSigloXXI
from ..models.Curriculo.Evaluacion_estudiantes import EvaluacionEstudiantes
from ..models.Curriculo.SostenibilidadCurriculo import SostenibilidadCurriculo

# FORMULARIO
from ..forms import Form_IngenieriaAula
from ..forms import Form_DesarrolloCiudadania
from ..forms import Form_CurriculoProgresivo
from ..forms import Form_CurriculoPropio 
from ..forms import Form_EvaluacionEstudiantes

# VISTA DE LOS SUBCRITERIOS
class CurriculoListView(generic.ListView):
    model = InclusionIngenieriaAula
    context_object_name = 'Curriculo_list'
    template_name = 'database/Curriculo/Curriculo_list.html'

# 2.1 CONSIDERACIONES SOBRE LAS ÁREAS Y LAS ASIGNATURAS
class ConsideracionesSobreAreasYAsignaturasListView(generic.ListView):
    model = ConsideracionesSobreAreasYAsignaturas
    context_object_name = 'ConsideracionesSobreAreasYAsignaturas_list'
    template_name ='database/Curriculo/ConsideracionesSobreAreasYAsignaturas_list.html'

# 2.2 Inclusion ingenieria aula
class InclusionIngenieriaAulaListView(generic.ListView):
    model = InclusionIngenieriaAula
    context_object_name = 'Inclusion_ingenieria_aula_list'
    template_name = 'database/Curriculo/Inclusion_ingenieria_aula_list.html'
    ordering = ['codigo']
    def get_queryset(self):
        return InclusionIngenieriaAula.objects.all().order_by('codigo')

    # FORMULARIO
def IngenieriaAula_new(request):
    if request.method == "POST":
        form_new = Form_IngenieriaAula(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizaje-centrado')
    else:
        form_new = Form_IngenieriaAula ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '2200 - INCLUSIÓN DE LA INGENIERÍA EN EL AULA'})

# 2.3 Desarrollo ciudadania digital
class DesarrolloCiudadaniaDigitalListView(generic.ListView):
    model = DesarrolloCiudadaniaDigital
    context_object_name = 'Desarrollo_ciudadania_digital_list'
    template_name = 'database/Curriculo/Desarrollo_ciudadania_digital_list.html'
    ordering = ['codigo']
    def get_queryset(self):
        return DesarrolloCiudadaniaDigital.objects.all().order_by('codigo')
    
    # FORMULARIO
def CiudadaniaDigital_new(request):
    if request.method == "POST":
        form_new = Form_DesarrolloCiudadania(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizaje-centrado')
    else:
        form_new = Form_DesarrolloCiudadania ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '2300 - DESARROLLO DE UNA CIUDADANÍA DIGITAL'})

# 2.4 INTEGRACIÓN CURRICULAR
class IntegracionCurricularListView(generic.ListView):
    model = Integracioncurricular
    context_object_name = 'IntegracionCurricular_list'
    template_name = 'database/Curriculo/IntegracionCurricular_list.html'

# 2.5 CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES
class CurriculoProgresivoListView(generic.ListView):
    model = CurriculoProgresivo
    context_object_name = 'Curriculo_progresivo_list'
    template_name = 'database/Curriculo/Curriculo_progresivo_list.html'
    ordering = ['codigo']
    def get_queryset(self):
        return CurriculoProgresivo.objects.all().order_by('codigo')

    # FORMULARIO
def CurriculoProgresivo_new(request):
    if request.method == "POST":
        form_new = Form_CurriculoProgresivo(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizaje-centrado')
    else:
        form_new = Form_CurriculoProgresivo ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '2500 - CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES'})

# 2.6 CURRÍCULO PROPIO
class CurriculoPropioListView(generic.ListView):
    model = CurriculoPropio
    context_object_name = 'Curriculo_propio_list'
    template_name = 'database/Curriculo/Curriculo_propio_list.html'
    ordering = ['codigo']
    def get_queryset(self):
        return CurriculoPropio.objects.all().order_by('codigo')

    # FORMULARIO
def CurriculoPropio_new(request):
    if request.method == "POST":
        form_new = Form_CurriculoPropio(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizaje-centrado')
    else:
        form_new = Form_CurriculoPropio ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '2600 - CURRÍCULO PROPIO'})

# 2.7 DESARROLLO DE LAS HABILIDADES DEL SIGLO XXI
class DesarrolloHabilidadesSigloXXIListView(generic.ListView):
    model = DesarroloHabilidadesSigloXXI
    context_object_name = 'DesarrolloHabilidadesSigloXXI_list'
    template_name = 'database/curriculo/DesarrolloHabilidadesSigloXXI_list.html'

# 2.8 EVALUACIÓN DE LOS ESTUDIANTES
class EvaluacionEstudiantesListView(generic.ListView):
    model = EvaluacionEstudiantes
    context_object_name = 'Evaluacion_estudiantes_list'
    template_name = 'database/Curriculo/Evaluacion_estudiantes_list.html'
    ordering = ['codigo']
    def get_queryset(self):
        return EvaluacionEstudiantes.objects.all().order_by('codigo')

    # FORMULARIO
def EvaluacionEstudiantes_new(request):
    if request.method == "POST":
        form_new = Form_EvaluacionEstudiantes(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizaje-centrado')
    else:
        form_new = Form_EvaluacionEstudiantes ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '2800 - EVALUACIÓN DE LOS ESTUDIANTES'})


# 2.9 SOSTENIBILIDAD - CURRÍCULO
class SostenibilidadCurriculoListView(generic.ListView):
    model = SostenibilidadCurriculo
    context_object_name = 'SostenibilidadCurriculo_list'
    template_name = 'database/Curriculo/SostenibilidadCurriculo_list.html'
