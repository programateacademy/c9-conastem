from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Personal_Docente_y_Administrativo.ApoyoPedagogicoParaelPersonal import ApoyoPedagogico
from ..models.Personal_Docente_y_Administrativo.DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales import DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales
from ..models.Personal_Docente_y_Administrativo.ProfesionalesEspecializadosEducacionSTEM import ProfesionalesEspecializadosEducacionSTEM
from ..models.Personal_Docente_y_Administrativo.SostenibilidadDocenteAdministrativo import SostenibilidadDocenteAdministrativo

class PersonalDocenteyAdministrativoListView (generic.ListView):
    model=ApoyoPedagogicoParaelPersonal
    context_object_name='ApoyoPedagogicoParaelPersonal'
    template_name='database/PersonalDocenteyAdministrativo/PersonalDocenteyAdministrativo.html'


class ApoyoPedagogicoListView (generic.ListView):
    model=ApoyoPedagogicoParaelPersonal
    context_object_name='ApoyoPedagogico_List'
    template_name='database/PersonalDocenteyAdministrativo/ApoyoPedagogico_List.html'

class DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionalesListView (generic.ListView):
    model=DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales
    context_object_name='DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales_list'
    template_name='database/PersonalDocenteyAdministrativo/DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales_list.html'


class ProfesionalesEspecializadosEducacionSTEMListView (generic.ListView):
    model=ProfesionalesEspecializadosEducacionSTEM
    context_object_name='ProfesionalesEspecializadosEducacionSTEM_List'
    template_name='database/PersonalDocenteyAdministrativo/ProfesionalesEspecializadosEducacionSTEM_List.html'

class SostenibilidadPersonalDocenteyAdministrativoListView (generic.ListView):
    model=SostenibilidadDocenteAdministrativo
    context_object_name='SostenibilidadDocenteAdministrativo_List'
    template_name='database/PersonalDocenteyAdministrativo/SostenibilidadDocenteAdministrativo_List.html'
