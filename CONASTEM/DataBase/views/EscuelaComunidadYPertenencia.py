from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Escuela_Comunidad_y_Pertenencia.CompromisodelaComunidad import CompromisodelaComunidad
from ..models.Escuela_Comunidad_y_Pertenencia.ConvivenciaEscolar import ConvivenciaEscolar
from ..models.Escuela_Comunidad_y_Pertenencia.RelacionesconlaComunidad import RelacionesconlaCominudad
from ..models.Escuela_Comunidad_y_Pertenencia.Sostenibilidad_EscuelaComunidadyPertenencia import SostenibilidadEscuelaComunidadyPertenencia

class EscuelaComunidadyPertenenciaListView(generic.ListView):
    model=CompromisodelaComunidad
    context_object_name='EscuelaComunidadyPertenencia'
    template_name='database\EscuelaComunidadyPertenencia\EscuelaComunidadyPertenencia.html'


class CompromisodelaComunidadListView (generic.ListView):
    model=CompromisodelaComunidad
    context_object_name='Compromisodelacomunidad_List'
    template_name='database\EscuelaComunidadyPertenencia\Compromisodelacomunidad_List.html'

class ConvivenciaescolarListView (generic.ListView):
    model=ConvivenciaEscolar
    context_object_name='Convivenciaescolar_List'
    template_name='database\EscuelaComunidadyPertenencia\Convivenciaescolar_List.html'

class RelacionesconlaComunidadListView (generic.ListView):
    model=RelacionesconlaCominudad
    context_object_name='Relacionesconlacomunidad_List'
    template_name='database\EscuelaComunidadyPertenencia\Relacionesconlacomunidad_List.html'

class SostenibilidadEscuelaComunidadyPertenenciaListView (generic.ListView):
    model=SostenibilidadEscuelaComunidadyPertenencia
    context_object_name='Sostenibilidadescuelacomunidadypertenenecia_List'
    template_name='database\EscuelaComunidadyPertenencia\Sostenibilidadescuelacomunidadypertenencia_List.html'
