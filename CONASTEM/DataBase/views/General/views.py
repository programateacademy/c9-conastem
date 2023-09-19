from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from ...models.Criterio import Criterio
from ...forms import FormPersonResponsable
from ...models.Person_Responsable import PersonResponsable
from ...models.Register import Register
from ...forms import FormRegister
from django.utils import timezone



class CriterioList(generic.ListView):
    model= Criterio
    context_object_name= 'criterio_list'
    template_name= 'home.html'

# VISTAS PERSONA RESPONSABLE
def person_responsablenew(request):
    if request.method == "POST":
        form = FormPersonResponsable(request.POST)
        if form.is_valid():
            print ('es valido')
            form.save()
            print ('se guarda')
            return HttpResponseRedirect('/database/responsables')
    else: 
        form = FormPersonResponsable()
    return render(request, 'person_responsable_new.html', {'form' : form})

class PersonResponsableDetail(generic.DetailView):
    model = PersonResponsable
    context_object_name = 'responsable_detail'
    template_name = 'person_responsable_detail.html'

class PersonResponsableListView(generic.ListView):
    model = PersonResponsable
    context_object_name = 'responsable_list'
    template_name = 'person_responsable_list.html'

# VISTAS DE REGISTRO DE INSTITUCIONES
class RegisterListView(generic.ListView):
    model = Register
    context_object_name= 'register_list'
    template_name= 'records.html'

class RegisterListDetail(generic.DetailView):
    model = Register
    context_object_name = 'register_detail'
    template_name= 'records_detail.html'

def index(request):
    if request.method == "POST":
        form = FormRegister(request.POST)
        if form.is_valid():
            register = form.save (commit=False)
            register.created_date = timezone.now()
            register.save()
            return HttpResponseRedirect('/database/instituciones/')
    else:
        form = FormRegister ()
    return render(request, 'registro_new.html', {'form': form})