from django.http import HttpResponseRedirect
from ..forms import Form_Criterio_3
from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from ..models.Formacion_Instruccion_Evaluacion.AprendizajeCentradoEstudiante import AprendizajeCentrado
from ..models.Formacion_Instruccion_Evaluacion.EducacionSTEMIntegrada import EducacionStemIntegrada
from ..models.Formacion_Instruccion_Evaluacion.TecnologiaFormacionInstruccion import TecnologiaFormacion
from ..models.Formacion_Instruccion_Evaluacion.EleccionCarrera import EleccionCarrera
from ..models.Formacion_Instruccion_Evaluacion.Sostenibilidad import SostenibilidadFormacionInstruccion


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

# VISTA DE EDUCACIÓN STEM INTEGRADA
class EducacionStemIntegradaListView(generic.ListView):
    model = EducacionStemIntegrada
    context_object_name = 'educacion_stem_integrada_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/educacion_stem_integrada.html'

# VISTA DE TECNOLOGÍA PARA LA FORMACIÓN / INSTRUCCIÓN
class TecnologiaFormacionListView(generic.ListView):
    model = TecnologiaFormacion
    context_object_name = 'Tecnologia_para_Formacion_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/tecnologia_para_formacion.html'

# VISTA DE ELECCIÓN DE CARRERA
class EleccionCarreraListView(generic.ListView):
    model = EleccionCarrera
    context_object_name= 'eleccion_carrera_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/eleccion_carrera.html'

# VISTA DE SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN
class SostenibilidadListView(generic.ListView):
    model = SostenibilidadFormacionInstruccion
    context_object_name = 'sostenibilidad_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/sostenibilidad.html'

# FORMULARIO
def data_new(request):
    if request.method == "POST":
        form_new = Form_Criterio_3(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/formacion-instruccion-evaluacion/')
    else:
        form_new = Form_Criterio_3 ()
    return render(request, 'database/Formacion_Instruccion_Evaluacion/aprendizaje_centrado_new.html', {'form_new': form_new})