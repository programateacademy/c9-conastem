from django.http import HttpResponseRedirect
from ..forms import Form_Criterio_3
from django.shortcuts import render
from django.utils import timezone


def data_new(request):
    if request.method == "POST":
        form_new = Form_Criterio_3(request.POST)
        if form_new.is_valid():
            data = form_new.save (commit=False)
            data.created_at = timezone.now()
            data.save()
            return HttpResponseRedirect('/database/criterios/')
    else:
        form_new = Form_Criterio_3 ()
    return render(request, 'aprendizaje_centrado_new.html', {'form': form_new})