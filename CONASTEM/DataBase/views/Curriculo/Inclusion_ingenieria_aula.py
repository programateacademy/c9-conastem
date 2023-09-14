from django.shortcuts import render
from django.views.generic import ListView
from DataBase.models.Curriculo.Inclusion_ingenieria_aula import ConcreteInclusionIngenieriaAula
from DataBase.models.Curriculo import Inclusion_ingenieria_aula

class InclusionIngenieriaAulaListView(ListView):

    model = Inclusion_ingenieria_aula
    template_name = 'Inclusion_ingenieria_aula_list.html' # Create this template
    context_object_name = 'inclusion_ingenieria_aula_list'

    # Query objects of the ConcreteInclusionIngenieriaAula model
    queryset = ConcreteInclusionIngenieriaAula.objects.all()
    # Rest of your view code...