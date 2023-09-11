from django.shortcuts import render
from django.views.generic import ListView

from ...models.Curriculo import Desarrollo_ciudadania_digital

class DesarrolloCiudadaniaDigitalListView(ListView):
    model = Desarrollo_ciudadania_digital
    template_name = 'desarrollo_ciudadania_digital_list.html'  # Create this template
    context_object_name = 'desarrollo_ciudadania_digital_list'
