from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

# MODELOS
from ..models.Personal_Docente_y_Administrativo.ApoyoPedagogico import ApoyoPedagogico
from ..models.Personal_Docente_y_Administrativo.DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales import DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales
from ..models.Personal_Docente_y_Administrativo.ProfesionalesEspecializadosEducacionSTEM import ProfesionalesEspecializadosEducacionSTEM
from ..models.Personal_Docente_y_Administrativo.SostenibilidadDocenteAdministrativo import SostenibilidadDocenteAdministrativo

# FORMULARIOS
from ..forms import Form_ApoyoPedagogico
from ..forms import Form_DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales
from ..forms import Form_ProfesionalesEspecializadosEducacionSTEM
from ..forms import Form_SostenibilidadDocenteAdministrativo


# VISTA DE LOS SUBCRITERIOS
class PersonalDocenteyAdministrativoListView (generic.ListView):
    model=ApoyoPedagogico
    context_object_name='PersonalDocenteAdministrativo_List'
    template_name='database/PersonalDocenteyAdministrativo/PersonalDocenteyAdministrativo.html'





# VISTA DE APOYO PEDAGÓGICO PARA EL PERSONAL
class ProfesionalesEspecializadosEducacionSTEMListView (generic.ListView):
    model=ApoyoPedagogico
    context_object_name='ApoyoPedagogico_List'
    template_name='database/PersonalDocenteyAdministrativo/ApoyoPedagogico_List.html'
    ordering = ['codigo']
    def get_queryset(self):
        return ProfesionalesEspecializadosEducacionSTEM.objects.all().order_by('codigo')

    # FORMULARIO 
def ProfesionalesespecializadoseducacionSTEM_new(request):
    if request.method == "POST":
        form_new = Form_ProfesionalesEspecializadosEducacionSTEM(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/profesional-calificado-educacion-stem')
    else:
        form_new = Form_ProfesionalesEspecializadosEducacionSTEM ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '4100 - PROFESIONALES ALTAMENTE CALIFICADOS ESPECIALIZADOS EN EDUCACIÓN STEM'})

# 4.2 DESARROLLO PROFESIONAL INICIAL Y CONTINUO PARA DOCENTES, DIRECTORES DE ESCUELA Y CONSEJEROS PROFESIONALES
class DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionalesListView (generic.ListView):
    model=DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales
    context_object_name='DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales_list'
    template_name='database/PersonalDocenteyAdministrativo/DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales_list.html'
    ordering = ['codigo']
    def get_queryset(self):
        return DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales.objects.all().order_by('codigo')

    # FORMULARIO
def Desaprofesionaldocentesdirectoresdeescuelaconsejerosprofesionales_new(request):
    if request.method == "POST":
        form_new = Form_DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/desarrollo-profesional-docentes-directores-consejeros-profesionales')
    else:
        form_new = Form_DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '4200 - DESARROLLO PROFESIONAL INICIAL Y CONTINUO PARA DOCENTES, DIRECTORES DE ESCUELA Y CONSEJEROS PROFESIONALES'})

# 4.3 APOYO PEDAGÓGICO PARA EL PERSONAL
class ApoyoPedagogicoListView (generic.ListView):
    model=ApoyoPedagogico
    context_object_name='ApoyoPedagogico_List'
    template_name='database/PersonalDocenteyAdministrativo/ApoyoPedagogico_List.html'
    ordering = ['codigo']
    def get_queryset(self):
        return ApoyoPedagogico.objects.all().order_by('codigo')

    # FORMULARIO
def Apoyopedagogico_new(request):
    if request.method == "POST":
        form_new = Form_ApoyoPedagogico(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/apoyo-pedagogico')
    else:
        form_new = Form_ApoyoPedagogico ()
    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '4300 - APOYO PEDAGÓGICO PARA EL PERSONAL'})

# 4.4 SOSTENIBILIDAD - PERSONAL DOCENTE Y ADMINISTRATIVO
class SostenibilidadDocenteAdministrativoListView (generic.ListView):
    model=SostenibilidadDocenteAdministrativo
    context_object_name='SostenibilidadDocenteAdministrativo_List'
    template_name='database/PersonalDocenteyAdministrativo/SostenibilidadDocenteAdministrativo_List.html'
    ordering = ['codigo']
    def get_queryset(self):
        return SostenibilidadDocenteAdministrativo.objects.all().order_by('codigo')

    # FORMULARIO 
def  Sostenibilidaddocenteadministrativo_new(request):
    if request.method == "POST":
        form_new = Form_SostenibilidadDocenteAdministrativo(request.POST)
        if form_new.is_valid():
            form_new.save()
            return HttpResponseRedirect('/database/sostenibilidad-docente-administrativo')
    else:
        form_new = Form_SostenibilidadDocenteAdministrativo ()

    return render(request, 'Form_Subcriterio.html', {'form_new': form_new, 'titulo': '4400 - SOSTENIBILIDAD - PERSONAL DOCENTE Y ADMINISTRATIVO'})