from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from ..models.Person_Responsable import PersonResponsable
from ..models.Criterio import Criterio
from ..models.Register import Register

from ..forms import FormRegister
from ..forms import FormPersonResponsable


# LISTA DE CRITERIOS
class CriterioList(generic.ListView):
    model= Criterio
    context_object_name= 'criterio_list'
    template_name= 'home.html'

# PERSONA RESPONSABLE
    # LISTA
class PersonResponsableDetail(generic.DetailView):
    model = PersonResponsable
    context_object_name = 'responsable_detail'
    template_name = 'person_responsable_detail.html'
    # DETALLE
class PersonResponsableListView(generic.ListView):
    model = PersonResponsable
    context_object_name = 'responsable_list'
    template_name = 'person_responsable_list.html'

    # FORMULARIO
def person_responsablenew(request):
    if request.method == "POST":
        form = FormPersonResponsable(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/database/responsables')
    else: 
        form = FormPersonResponsable()
    return render(request, 'person_responsable_new.html', {'form' : form})

# REGISTRO DE INSTITUCIONES
    # LISTA
class RegisterListView(generic.ListView):
    model = Register
    context_object_name= 'register_list'
    template_name= 'records_list.html'
    # DETALLE
class RegisterListDetail(generic.DetailView):
    model = Register
    context_object_name = 'register_detail'
    template_name= 'records_detail.html'

    # FORMULARIO
def index(request):
    if request.method == "POST":
        form = FormRegister(request.POST)
        if form.is_valid():
            register = form.save (commit=False)
            register.created_date = timezone.now()
            register.save()
            return HttpResponseRedirect('/database/home')
    else:
        form = FormRegister ()
    return render(request, 'records_new.html', {'form': form})