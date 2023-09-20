from django.http import HttpResponseRedirect
# from ..forms import Form_Criterio_3
from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from ..models.Formacion_Instruccion_Evaluacion.AprendizajeCentradoEstudiante import AprendizajeCentrado
from ..models.Formacion_Instruccion_Evaluacion.EducacionSTEM import EducacionSTEMIntegrada
from ..models.Formacion_Instruccion_Evaluacion.ApredizajeRiguroso import AprendizajeRiguroso
from ..models.Formacion_Instruccion_Evaluacion.PlaneacionyCreaciondeActividades import PlaneacionyCreaciondeActividades
from ..models.Formacion_Instruccion_Evaluacion.EstrategiasFormativas import EstrategiasFormativas
from ..models.Formacion_Instruccion_Evaluacion.AprendizajeExtendido import AprendizajeExtendido

from ..models.Formacion_Instruccion_Evaluacion.TecnologiaFormacionInstruccion import TecnologiaFormacion
from ..models.Formacion_Instruccion_Evaluacion.EleccionCarrera import EleccionCarrera
from ..models.Formacion_Instruccion_Evaluacion.Sostenibilidad import SostenibilidadFormacionInstruccion

# FORMULARIO
from ..forms import Form_AprendizajeCentrado
from ..forms import Form_Aprendizajeriguroso
from ..forms import Form_Aprendizajeextendido
from ..forms import Form_Estrategiasformativas
from ..forms import Form_Planeacionycreaciondeactividades


# VISTA DE LOS SUBCITERIOS
class FormacionInstruccionEvaluacionListView(generic.ListView):
    model = AprendizajeCentrado
    context_object_name = 'FormacionInstruccionEvaluacion'
    template_name = 'database/Formacion_Instruccion_Evaluacion/formacion_instruccion_evaluacion_list.html'

# VISTA DE APRENDIZAJE CENTRADO EN EL ESTUDIANTE
class AprendizajeCentradoListView(generic.ListView):
    model = AprendizajeCentrado
    context_object_name = 'aprendizaje_centrado_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/aprendizaje_centrado.html'

# VISTA DE APRENDIZAJE RIGUROSO
class AprendizajeRigurosoListView(generic.ListView):
    model=AprendizajeRiguroso
    context_object_name='AprendizajeRiguroso_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Aprendizajeriguroso_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return AprendizajeRiguroso.objects.all().order_by('codigo')
    
def Aprendizajeriguroso_new(request):
  
    if request.method == "POST":
        form_new = Form_Aprendizajeriguroso(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizajeriguroso')
    else:
        form_new = Form_Aprendizajeriguroso()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3200-APRENDIZAJE RIGUROSO'})



# VISTA DE PLANEACIÓN Y CREACIÓN DE ACTIVIDADES
class PlaneacionyCreaciondeActividadesListView(generic.ListView):
    model=PlaneacionyCreaciondeActividades
    context_object_name='PlaneacionyCreaciondeActividades_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Planeacionycreaciondeactividades_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return PlaneacionyCreaciondeActividades.objects.all().order_by('codigo')
    
def Planeacionycreaciondeactividades_new(request):
  
    if request.method == "POST":
        form_new = Form_Planeacionycreaciondeactividades(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/planeacionycreaciondeactividades')
    else:
        form_new = Form_Planeacionycreaciondeactividades()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3300-PLANEACION Y CREACIÓN DE ACTIVIDADES'})


# VISTA DE EDUCACIÓN STEM INTEGRADA
class EducacionStemIntegradaListView(generic.ListView):
    model = EducacionSTEMIntegrada
    context_object_name = 'educacion_stem_integrada_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/educacion_stem_integrada.html'

# VISTA DE TECNOLOGÍA PARA LA FORMACIÓN / INSTRUCCIÓN
class TecnologiaFormacionListView(generic.ListView):
    model = TecnologiaFormacion
    context_object_name = 'Tecnologia_para_Formacion_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/tecnologia_para_formacion.html'

# VISTA DE ESTRATEGIAS FORMATIVAS
class EstrategiasFormativasListView(generic.ListView):
    model=EstrategiasFormativas
    context_object_name='EstrategiasFormativas_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Estrategiasformativas_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return EstrategiasFormativas.objects.all().order_by('codigo')
    
def Estrategiasformativas_new(request):
  
    if request.method == "POST":
        form_new = Form_Estrategiasformativas(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/estrategiasformativas')
    else:
        form_new = Form_Estrategiasformativas()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3600-ESTRATEGIAS FORMATIVAS'})



# VISTA DE ELECCIÓN DE CARRERA
class EleccionCarreraListView(generic.ListView):
    model = EleccionCarrera
    context_object_name= 'eleccion_carrera_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/eleccion_carrera.html'

# VISTA DE APRENDIZAJE EXTENDIDO
class AprendizajeExtendidoListView(generic.ListView):
    model=AprendizajeExtendido
    context_object_name='AprendizajeExtendido_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Aprendizajeextendido_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return AprendizajeExtendido.objects.all().order_by('codigo')

def Aprendizajeextendido_new(request):
  
    if request.method == "POST":
        form_new = Form_Aprendizajeextendido(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizajeextendido')
    else:
        form_new = Form_Aprendizajeextendido()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo':'3800-APRENDIZAJE EXTENDIDO'})



# VISTA DE SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN
class SostenibilidadListView(generic.ListView):
    model = SostenibilidadFormacionInstruccion
    context_object_name = 'sostenibilidad_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/sostenibilidad.html'

# FORMULARIO
# def data_new(request):
#     if request.method == "POST":
#         form_new = Form_Criterio_3(request.POST)
#         if form_new.is_valid():
#             form_new.save()
#             return HttpResponseRedirect('/database/formacion-instruccion-evaluacion/')
#     else:
#         form_new = Form_Criterio_3 ()

    # return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': 'APRENDIZAJE CENTRADO EN EL ESTUDIANTE'})
