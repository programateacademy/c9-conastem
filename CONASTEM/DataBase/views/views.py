from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

# Create your views here.

from ..models.Infraestructura.Equidad import Equidad
from ..models.Criterio import Criterio

def index(request):
    return HttpResponse("Hello, World!")
    
    class CriterioList(generic.ListView):
        model= Criterio
        context_object_name= 'criterio_list'
        template_name= 'index.html'