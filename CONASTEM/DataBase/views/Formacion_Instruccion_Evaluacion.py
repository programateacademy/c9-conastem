from django.http import HttpResponseRedirect
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

# VISTA DE PLANEACIÓN Y CREACIÓN DE ACTIVIDADES
class PlaneacionyCreaciondeActividadesListView(generic.ListView):
    model=PlaneacionyCreaciondeActividades
    context_object_name='PlaneacionyCreaciondeActividades_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Planeacionycreaciondeactividades_List.html'

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

# VISTA DE SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN
class SostenibilidadListView(generic.ListView):
    model = SostenibilidadFormacionInstruccion
    context_object_name = 'sostenibilidad_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/sostenibilidad.html'

# FORMULARIO
def Aprendizajecentrado_new(request):
    if request.method == "POST":
        form_new = Form_AprendizajeCentrado(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/aprendizaje-centrado')
    else:
        form_new = Form_AprendizajeCentrado ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': 'APRENDIZAJE CENTRADO EN EL ESTUDIANTE'})
