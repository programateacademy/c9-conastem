from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic

# Create your views here.
from ..models.Escuela_Comunidad_y_Pertenencia.CompromisodelaComunidad import CompromisodelaCominudad


class CompromisodelaComunidadListView (generic.ListView):
    model=CompromisodelaCominudad
    context_object_name='Compromiso_de_la_comunidad'
    template_name='database\EscuelaComunidadyPertenencia\Compromiso_de_la_comunidad.html'