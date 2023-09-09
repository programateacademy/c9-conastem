from django.shortcuts import render
<<<<<<< HEAD
from django.views import generic
=======

# Create your views here.

from ..models.INFRAESTRUCTURA.Equidad import Equidad
>>>>>>> 5b9c164413a0b8f059e2c738262412d5491e3f7a
from ..models.Criterio import Criterio


class CriterioList(generic.ListView):
    model= Criterio
    context_object_name= 'criterio_list'
    template_name= 'index.html'