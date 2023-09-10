from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ...models.Curriculo.Inclusion_ingenieria_aula import Inclusion_ingenieria_aula

class InclusionIngenieriaAulaListView(ListView):
    model = Inclusion_ingenieria_aula
    template_name = 'databases\Curriculo\inclusion_ingenieria_aula_list.html'
    context_object_name = 'inclusiones'

class InclusionIngenieriaAulaDetailView(DetailView):
    model = Inclusion_ingenieria_aula
    template_name = 'databases\inclusion_ingenieria_aula_detail.html'

class InclusionIngenieriaAulaCreateView(CreateView):
    model = Inclusion_ingenieria_aula
    template_name = 'databases\inclusion_ingenieria_aula_form.html'
    fields = ['numeral']  # Agrega los campos que desees mostrar en el formulario de creación

class InclusionIngenieriaAulaUpdateView(UpdateView):
    model = Inclusion_ingenieria_aula
    template_name = 'databases\inclusion_ingenieria_aula_form.html' 
    fields = ['numeral']  # Agrega los campos que desees mostrar en el formulario de actualización

class InclusionIngenieriaAulaDeleteView(DeleteView):
    model = Inclusion_ingenieria_aula
    template_name = 'databases\inclusion_ingenieria_aula_confirm_delete.html'  # Cambia 'tu_app' al nombre de tu aplicación
    success_url = '/lista_inclusiones/'  # Cambia esta URL a la que desees redirigir después de la eliminación
