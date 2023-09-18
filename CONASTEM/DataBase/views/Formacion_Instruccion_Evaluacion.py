from django.http import HttpResponseRedirect
from ..forms import Form_Criterio_3
from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from ..models.Formacion_Instruccion_Evaluacion.AprendizajeCentradoEstudiante import AprendizajeCentrado
from ..models.Formacion_Instruccion_Evaluacion.ApredizajeRiguroso import AprendizajeRiguroso
from ..models.Formacion_Instruccion_Evaluacion.PlaneacionyCreaciondeActividades import PlaneacionyCreaciondeActividades
from ..models.Formacion_Instruccion_Evaluacion.EstrategiasFormativas import EstrategiasFormativas
from ..models.Formacion_Instruccion_Evaluacion.AprendizajeExtendido import AprendizajeExtendido
from ..models.Formacion_Instruccion_Evaluacion.EducacionSTEMIntegrada import EducacionStemIntegrada
from ..models.Formacion_Instruccion_Evaluacion.TecnologiaFormacionInstruccion import TecnologiaFormacion


# Vista de lista
class FormacionInstruccionEvaluacionListView(generic.ListView):
    model = AprendizajeCentrado
    context_object_name = 'FormacionInstruccionEvaluacion'
    template_name = 'database/Formacion_Instruccion_Evaluacion/formacion_instruccion_evaluacion_list.html'

# Vista detalle Aprendizaje Centrado

class AprendizajeCentradoListView(generic.ListView):
    model = AprendizajeCentrado
    context_object_name = 'aprendizaje_centrado_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/aprendizaje_centrado.html'

# Formulario
def data_new(request):
    if request.method == "POST":
        form_new = Form_Criterio_3(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/formacion-instruccion-evaluacion/')
    else:
        form_new = Form_Criterio_3 ()
    return render(request, 'database/Formacion_Instruccion_Evaluacion/aprendizaje_centrado_new.html', {'form_new': form_new})

#Aprendizaje Riguroso 

class AprendizajeRigurosoListView(generic.ListView):
    model=AprendizajeRiguroso
    context_object_name='AprendizajeRiguroso_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Aprendizajeriguroso_List.html'

#Planeacion y Creación de actividades

class PlaneacionyCreaciondeActividadesListView(generic.ListView):
    model=PlaneacionyCreaciondeActividades
    context_object_name='PlaneacionyCreaciondeActividades_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Planeacionycreaciondeactividades_List.html'

#Estrategias Formativas

class EstrategiasFormativasListView(generic.ListView):
    model=EstrategiasFormativas
    context_object_name='EstrategiasFormativas_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Estrategiasformativas_List.html'

#Aprendizaje Extendido

class AprendizajeExtendidoListView(generic.ListView):
    model=AprendizajeExtendido
    context_object_name='AprendizajeExtendido_List'
    template_name='database\Formacion_Instruccion_Evaluacion\Aprendizajeextendido_List.html'


class EducacionStemIntegradaListView(generic.ListView):
    model = EducacionStemIntegrada
    context_object_name = 'educacion_stem_integrada_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/educacion_stem_integrada.html'

class TecnologiaFormacionListView(generic.ListView):
    model = TecnologiaFormacion
    context_object_name = 'Tecnologia_para_Formacion_list'
    template_name = 'database/Formacion_Instruccion_Evaluacion/tecnologia_para_formacion.html'
