from django.shortcuts import render
# Create your views here.

from ..models.Criterio import Criterio

def index (request):
    criterios= Criterio.objects.all()

    return render (
        request,
        'database/index.html',
        context=
        {
            "criterios": criterios
        }
    )