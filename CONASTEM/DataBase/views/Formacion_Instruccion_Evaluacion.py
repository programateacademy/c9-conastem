from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

# MODELOS
from ..models.Formacion_Instruccion_Evaluacion.AprendizajeCentradoEstudiante import AprendizajeCentrado
from ..models.Formacion_Instruccion_Evaluacion.EducacionSTEM import EducacionSTEMIntegrada
from ..models.Formacion_Instruccion_Evaluacion.ApredizajeRiguroso import AprendizajeRiguroso
from ..models.Formacion_Instruccion_Evaluacion.PlaneacionyCreaciondeActividades import PlaneacionyCreaciondeActividades
from ..models.Formacion_Instruccion_Evaluacion.EstrategiasFormativas import EstrategiasFormativas
from ..models.Formacion_Instruccion_Evaluacion.AprendizajeExtendido import AprendizajeExtendido
from ..models.Formacion_Instruccion_Evaluacion.TecnologiaFormacionInstruccion import TecnologiaFormacion
from ..models.Formacion_Instruccion_Evaluacion.EleccionCarrera import EleccionCarrera
from ..models.Formacion_Instruccion_Evaluacion.SostenibilidadFormacionInstruccion import SostenibilidadFormacionInstruccion

# FORMULARIO
from ..forms import Form_AprendizajeCentrado
from ..forms import Form_EducacionSTEM
from ..forms import Form_EleccionCarrera
from ..forms import Form_TecFormacionInstruccion
from ..forms import Form_SostenibilidadFormacion
from ..forms import Form_Aprendizajeriguroso
from ..forms import Form_Aprendizajeextendido
from ..forms import Form_Estrategiasformativas
from ..forms import Form_Planeacionycreaciondeactividades


# VISTA DE LOS SUBCITERIOS
class FormacionInstruccionEvaluacionListView(generic.ListView):
    model = AprendizajeCentrado
    context_object_name = 'FormacionInstruccionEvaluacion'
    template_name = 'database/Formacion_Instruccion_Evaluacion/formacion_instruccion_evaluacion_list.html'

# 3.1 APRENDIZAJE CENTRADO EN EL ESTUDIANTE
class AprendizajeCentradoListView(generic.ListView):
    model = AprendizajeCentrado
    context_object_name = 'aprendizaje_centrado_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/aprendizaje_centrado.html'
    ordering = ['codigo']
    def get_queryset(self):
        return AprendizajeCentrado.objects.all().order_by('codigo')

    # FORMULARIO
def Aprendizajecentrado_new(request):
    if request.method == "POST":
        form_new = Form_AprendizajeCentrado(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizaje-centrado')
    else:
        form_new = Form_AprendizajeCentrado ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '3100 - APRENDIZAJE CENTRADO EN EL ESTUDIANTE'})

# 3.2 APRENDIZAJE RIGUROSO
class AprendizajeRigurosoListView(generic.ListView):
    model=AprendizajeRiguroso
    context_object_name='AprendizajeRiguroso_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Aprendizajeriguroso_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return AprendizajeRiguroso.objects.all().order_by('codigo')
    
    # FORMULARIO
def Aprendizajeriguroso_new(request):
    if request.method == "POST":
        form_new = Form_Aprendizajeriguroso(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizajeriguroso')
    else:
        form_new = Form_Aprendizajeriguroso()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3200-APRENDIZAJE RIGUROSO'})

# 3.3 PLANEACIÓN Y CREACIÓN DE ACTIVIDADES
class PlaneacionyCreaciondeActividadesListView(generic.ListView):
    model=PlaneacionyCreaciondeActividades
    context_object_name='PlaneacionyCreaciondeActividades_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Planeacionycreaciondeactividades_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return PlaneacionyCreaciondeActividades.objects.all().order_by('codigo')

    # FORMULARIO
def Planeacionycreaciondeactividades_new(request):
    if request.method == "POST":
        form_new = Form_Planeacionycreaciondeactividades(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/planeacionycreaciondeactividades')
    else:
        form_new = Form_Planeacionycreaciondeactividades()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3300-PLANEACION Y CREACIÓN DE ACTIVIDADES'})

# 3.4 EDUCACIÓN STEM INTEGRADA
class EducacionStemIntegradaListView(generic.ListView):
    model = EducacionSTEMIntegrada
    context_object_name = 'educacion_stem_integrada_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/educacion_stem_integrada.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'
    def get_queryset(self):
        return EducacionSTEMIntegrada.objects.all().order_by('codigo')

    # FORMULARIO
def EducacionSTEM_new(request):
    if request.method == "POST":
        form_new = Form_EducacionSTEM(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/educacion-stem-integrada')
    else:
        form_new = Form_EducacionSTEM ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3400 - EDUCACIÓN STEM INTREGRADA'})

# 3.5 TECNOLOGÍA PARA LA FORMACIÓN / INSTRUCCIÓN
class TecnologiaFormacionListView(generic.ListView):
    model = TecnologiaFormacion
    context_object_name = 'Tecnologia_para_Formacion_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/tecnologia_para_formacion.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'
    def get_queryset(self):
        return TecnologiaFormacion.objects.all().order_by('codigo')

    # FORMULARIO
def TecnologiaFormacion_new(request):
    if request.method == "POST":
        form_new = Form_TecFormacionInstruccion(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/tecnologia-para-formacion')
    else:
        form_new = Form_TecFormacionInstruccion ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3500 - TECNOLOGÍA PARA LA FORMACIÓN / INSTRUCCIÓN'})

# 3.6 ESTRATEGIAS FORMATIVAS
class EstrategiasFormativasListView(generic.ListView):
    model=EstrategiasFormativas
    context_object_name='EstrategiasFormativas_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Estrategiasformativas_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return EstrategiasFormativas.objects.all().order_by('codigo')
    
    # FORMULARIO
def Estrategiasformativas_new(request):
    if request.method == "POST":
        form_new = Form_Estrategiasformativas(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/estrategiasformativas')
    else:
        form_new = Form_Estrategiasformativas()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3600-ESTRATEGIAS FORMATIVAS'})

# 3.7 ELECCIÓN DE CARRERA
class EleccionCarreraListView(generic.ListView):
    model = EleccionCarrera
    context_object_name= 'eleccion_carrera_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/eleccion_carrera.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'
    def get_queryset(self):
        return EleccionCarrera.objects.all().order_by('codigo')
    
    # FORMULARIO
def Eleccioncarrera_new(request):
    if request.method == "POST":
        form_new = Form_EleccionCarrera(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/eleccion-carrera')
    else:
        form_new = Form_EleccionCarrera ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3700 - ELECCIÓN DE CARRERA'})

# 3.8 APRENDIZAJE EXTENDIDO
class AprendizajeExtendidoListView(generic.ListView):
    model=AprendizajeExtendido
    context_object_name='AprendizajeExtendido_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Aprendizajeextendido_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return AprendizajeExtendido.objects.all().order_by('codigo')

    # FORMULARIO
def Aprendizajeextendido_new(request):
    if request.method == "POST":
        form_new = Form_Aprendizajeextendido(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizajeextendido')
    else:
        form_new = Form_Aprendizajeextendido()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3800-APRENDIZAJE EXTENDIDO'})

# 3.9 SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN
class SostenibilidadListView(generic.ListView):
    model = SostenibilidadFormacionInstruccion
    context_object_name = 'sostenibilidad_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/sostenibilidad.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'
    def get_queryset(self):
        return SostenibilidadFormacionInstruccion.objects.all().order_by('codigo')
    
    # FORMULARIO
def SostenibilidadFormacion_new(request):
    if request.method == "POST":
        form_new = Form_SostenibilidadFormacion(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/sostenibilidad-formacion-instruccion')
    else:
        form_new = Form_SostenibilidadFormacion ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3900 - SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN'})
