from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Curriculo.Inclusion_ingenireia_aula import Inclusion_ingenieria_aula

class Inclusion_ingenieria_aula_ListView (generic.ListView):
    model= Inclusion_ingenieria_aula
    context_object_name='Curriculo'
    template_name='database\Curriculo\Curriculo.html'
    # template_name = 'database/Curriculo/Curriculo.html'
    