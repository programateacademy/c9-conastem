from django.shortcuts import render
from django.views.generic import ListView

from ...models.Curriculo import Inclusion_ingenieria_aula

class InclusionIngenieriaAulaListView(ListView):
    model = Inclusion_ingenieria_aula
    template_name = 'inclusion_ingenieria_aula_list.html'  # Create this template
    context_object_name = 'inclusion_ingenieria_aula_list'
