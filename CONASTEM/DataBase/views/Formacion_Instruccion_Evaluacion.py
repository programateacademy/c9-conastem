from django.http import HttpResponseRedirect
from ..forms import Form_Criterio_3
from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from ..models.Formacion_Instruccion_Evaluacion.AprendizajeCentradoEstudiante import AprendizajeCentrado

# Vista de lista
class FormacionInstruccionEvaluacionListView(generic.ListView):
    model = AprendizajeCentrado
    context_object_name = 'FormacionInstruccionEvaluacion'
    template_name = 'database/Formacion_Instruccion_Evaluacion/formacion_instruccion_evaluacion_list.html'

# Vista detalle

class AprendizajeCentradoListView(generic.ListView):
    model = AprendizajeCentrado
    context_object_name = 'aprendizaje_centrado_detail'
    template_name = 'database/Formacion_Instruccion_Evaluacion/aprendizaje_centrado.html'

# Formulario
def data_new(request):
    if request.method == "POST":
        form_new = Form_Criterio_3(request.POST)
        if form_new.is_valid():
            data = form_new.save (commit=True)
            data.save()
            return HttpResponseRedirect('/database/home/')
    else:
        form_new = Form_Criterio_3 ()
    return render(request, 'database/Formacion_Instruccion_Evaluacion/aprendizaje_centrado_new.html', {'form_new': form_new})