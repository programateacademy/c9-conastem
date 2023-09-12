from django.shortcuts import render
from django.views.generic import ListView

from ...models.Curriculo import ConsideracionesSobreAreasYAsignaturas

class ConsideracionesSobreAreasyAsignaturasListView(ListView):
    model = ConsideracionesSobreAreasYAsignaturas
    template_name = 'ConsideracionesSobreAreasYAsignaturas.html'  # Create this template
    context_object_name = 'ConsideracionesSobreAreasYAsignaturas_list'
