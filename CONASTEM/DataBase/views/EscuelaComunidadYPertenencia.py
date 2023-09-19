from django.http import HttpResponseRedirect
from ..forms import Form_Compromisodelacomunidad
from ..forms import Form_Convivenciaescolar
from ..forms import Form_Relacionesconlacomunidad
from ..forms import Form_Sostenibilidadescuela
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
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return CompromisodelaComunidad.objects.all().order_by('codigo')

# FORMULARIO
def Compromisodelacomunidad_new(request):
  
    if request.method == "POST":
        form_new = Form_Compromisodelacomunidad(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/compromisodelacomunidad')
    else:
        form_new = Form_Compromisodelacomunidad ()

    return render(request, 'database/Form_Subcriterio.html', {'form_new': form_new, 'titulo':'Compromiso de la comunidad'})


class ConvivenciaescolarListView (generic.ListView):
    model=ConvivenciaEscolar
    context_object_name='Convivenciaescolar_List'
    template_name='database\EscuelaComunidadyPertenencia\Convivenciaescolar_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return ConvivenciaEscolar.objects.all().order_by('codigo')


def convivenciaescolarnew(request):
    if request.method == "POST":
        form_new = Form_Convivenciaescolar(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/convivenciaescolar')
    else:
        form_new = Form_Convivenciaescolar ()

    return render(request, 'database/Form_Subcriterio.html', {'form_new': form_new , 'titulo':'Convivencia Escolar'})


class RelacionesconlaComunidadListView (generic.ListView):
    model=RelacionesconlaComunidad
    context_object_name='Relacionesconlacomunidad_List'
    template_name='database\EscuelaComunidadyPertenencia\Relacionesconlacomunidad_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return RelacionesconlaComunidad.objects.all().order_by('codigo')

def relacionesconlacomunidadnew(request):
    if request.method == "POST":
        form_new = Form_Relacionesconlacomunidad(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/relacionesconlacomunidad')
    else:
        form_new = Form_Relacionesconlacomunidad ()

    return render(request, 'database/Form_Subcriterio.html', {'form_new': form_new , 'titulo':'Relaciones con la comunidad'})


class SostenibilidadEscuelaComunidadyPertenenciaListView (generic.ListView):
    model=SostenibilidadEscuelaComunidadyPertenencia
    context_object_name='Sostenibilidadescuelacomunidadypertenenecia_List'
    template_name='database\EscuelaComunidadyPertenencia\Sostenibilidadescuelacomunidadypertenencia_List.html'
    ordering = ['codigo']  # Ordena por el campo 'codigo'

    def get_queryset(self):
        return SostenibilidadEscuelaComunidadyPertenencia.objects.all().order_by('codigo')


def sostenibilidadescuelanew(request):
    if request.method == "POST":
        form_new = Form_Sostenibilidadescuela(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/sostenibilidadescuelacomunidadypertenencia')
    else:
        form_new = Form_Sostenibilidadescuela ()

    return render(request, 'database/Form_Subcriterio.html', {'form_new': form_new , 'titulo':'Sostenibilidad-Escuela, comunidad y compromiso'})
