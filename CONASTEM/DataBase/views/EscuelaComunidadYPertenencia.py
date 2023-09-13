from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Escuela_Comunidad_y_Pertenencia.CompromisodelaComunidad import CompromisodelaComunidad
from ..models.Escuela_Comunidad_y_Pertenencia.ConvivenciaEscolar import ConvivenciaEscolar
from ..models.Escuela_Comunidad_y_Pertenencia.RelacionesconlaComunidad import RelacionesconlaCominudad
from ..models.Escuela_Comunidad_y_Pertenencia.Sostenibilidad_EscuelaComunidadyPertenencia import Sostenibilidad_EscuelaComunidadyPertenencia

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

class Sostenibilidad_EscuelaComunidadyPertenencia (generic.ListView):
    model=Sostenibilidad_EscuelaComunidadyPertenencia
    context_object_name='Sostenibilidad_escuelacomunidadypertenenecia_List'
    template_name='database\EscuelaComunidadyPertenencia\Sostenibilidad_escuelacomunidadypertenencia_List.html'
