from django.views import generic
from django.shortcuts import render
from ...models.Criterio import Criterio




class CriterioList(generic.ListView):
    model= Criterio
    context_object_name= 'criterio_list'
    template_name= 'home.html'