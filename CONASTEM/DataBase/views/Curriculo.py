from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Curriculo.Inclusion_ingenieria_aula import InclusionIngenieriaAula
from ..models.Curriculo.Desarrollo_ciudadania_digital import DesarrolloCiudadaniaDigital
from ..models.Curriculo.Curriculo_progresivo import CurriculoProgresivo

class InclusionIngenieriaAulaListView(generic.ListView):
    model = InclusionIngenieriaAula
    context_object_name = 'Inclusion_ingenieria_aula_list'
    template_name = 'database/Curriculo/Inclusion_ingenieria_aula_list.html'

class DesarrolloCiudadaniaDigitalListView(generic.ListView):
    model = DesarrolloCiudadaniaDigital
    context_object_name = 'Desarrollo_ciudadania_digital_list'
    template_name = 'database/Curriculo/Desarrollo_ciudadania_digital_list.html'

class CurriculoProgresivoListView(generic.ListView):
    model = CurriculoProgresivo
    context_object_name = 'Curriculo_progresivo_list'
    template_name = 'database/Curriculo/Curriculo_progresivo_list.html'