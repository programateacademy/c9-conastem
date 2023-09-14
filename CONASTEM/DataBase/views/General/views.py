from django.views import generic
from django.shortcuts import render
from ...models.Criterio import Criterio

def home (request):
    criterios = Criterio.objects.all()

    return render(
        request,
        'home.html',
        context= {
            'criterios':criterios
        }
    )


class CriterioList(generic.ListView):
    model= Criterio
    context_object_name= 'criterio_list'
    template_name= 'criterios.html'