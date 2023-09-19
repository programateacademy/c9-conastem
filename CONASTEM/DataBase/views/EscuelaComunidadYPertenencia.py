from django.http import HttpResponseRedirect
from ..forms import Form_Compromisodelacomunidad
from ..forms import Form_Convivenciaescolar
from django.shortcuts import render
from django.views import generic
from django.utils import timezone


# Create your views here.
from ..models.Escuela_Comunidad_y_Pertenencia.CompromisodelaComunidad import CompromisodelaComunidad
from ..models.Escuela_Comunidad_y_Pertenencia.ConvivenciaEscolar import ConvivenciaEscolar
from ..models.Escuela_Comunidad_y_Pertenencia.RelacionesconlaComunidad import RelacionesconlaComunidad
from ..models.Escuela_Comunidad_y_Pertenencia.Sostenibilidad_EscuelaComunidadyPertenencia import SostenibilidadEscuelaComunidadyPertenencia

class EscuelaComunidadyPertenenciaListView(generic.ListView):
    model=CompromisodelaComunidad
    context_object_name='EscuelaComunidadyPertenencia'
    template_name='database\EscuelaComunidadyPertenencia\EscuelaComunidadyPertenencia.html'

class CompromisodelaComunidadListView (generic.ListView):
    model=CompromisodelaComunidad
    context_object_name='Compromisodelacomunidad_List'
    template_name='database\EscuelaComunidadyPertenencia\Compromisodelacomunidad_List.html'

# FORMULARIO
def data_new(request):
    contexto = {
    'titulo': 'Compromiso de la comunidad'
}
    if request.method == "POST":
        form_new = Form_Compromisodelacomunidad(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/compromisodelacomunidad')
    else:
        form_new = Form_Compromisodelacomunidad ()

    return render(request, 'database/EscuelaComunidadyPertenencia/Form_Subcriterio.html', {'form_new': form_new, 'titulo':'Compromiso de la comunidad'})


class ConvivenciaescolarListView (generic.ListView):
    model=ConvivenciaEscolar
    context_object_name='Convivenciaescolar_List'
    template_name='database\EscuelaComunidadyPertenencia\Convivenciaescolar_List.html'

def convivenciaescolarnew(request):
    if request.method == "POST":
        form_new = Form_Convivenciaescolar(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/convivenciaescolar')
    else:
        form_new = Form_Convivenciaescolar ()

    return render(request, 'database/EscuelaComunidadyPertenencia/Form_Subcriterio.html', {'form_new': form_new , 'titulo':'Convivencia Escolar'})


class RelacionesconlaComunidadListView (generic.ListView):
    model=RelacionesconlaComunidad
    context_object_name='Relacionesconlacomunidad_List'
    template_name='database\EscuelaComunidadyPertenencia\Relacionesconlacomunidad_List.html'

class SostenibilidadEscuelaComunidadyPertenenciaListView (generic.ListView):
    model=SostenibilidadEscuelaComunidadyPertenencia
    context_object_name='Sostenibilidadescuelacomunidadypertenenecia_List'
    template_name='database\EscuelaComunidadyPertenencia\Sostenibilidadescuelacomunidadypertenencia_List.html'
