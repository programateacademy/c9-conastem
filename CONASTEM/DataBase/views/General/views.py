from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render
from ...models.Criterio import Criterio
from ...forms import FormPersonResponsable
from ...models.Person_Responsable import PersonResponsable



class CriterioList(generic.ListView):
    model= Criterio
    context_object_name= 'criterio_list'
    template_name= 'home.html'

def person_responsablenew(request):
    if request.method == "POST":
        form = FormPersonResponsable(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/database/home')
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