from django.http import HttpResponseRedirect
from django.views import generic
from ...models.Register import Register
from ...forms import FormRegister
from django.shortcuts import render
from django.utils import timezone


class RegisterListView(generic.ListView):
    model = Register
    context_object_name= 'register_list'
    template_name= 'records.html'

class RegisterListDetail(generic.DetailView):
    model = Register
    context_object_name = 'register_detail'
    template_name= 'records_detail.html'

def index(request):
    if request.method == "POST":
        form = FormRegister(request.POST)
        if form.is_valid():
            register = form.save (commit=False)
            register.created_date = timezone.now()
            register.save()
            return HttpResponseRedirect('/database/instituciones/')
    else:
        form = FormRegister ()
    return render(request, 'record_new.html', {'form': form})